import numpy as np
from typing import List, Dict, Any, Optional, TYPE_CHECKING
import re
import logging
import base64
import hashlib
from datetime import datetime, timezone
import random as _random
import math as _math

try:
    from cryptography.fernet import Fernet  # type: ignore
except Exception:
    Fernet = None  # cryptography optional

if TYPE_CHECKING:
    # Only for type-checkers; at runtime Fernet may be None
    from cryptography.fernet import Fernet as _Fernet

# Secure logging: local file only. Keep format stable and include UTC timestamp
logging.basicConfig(
    filename='ragsecure_audit.log',
    level=logging.WARNING,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filemode='a'
)

class EncryptedVectorStore:
    """Encrypted vector store with optional Fernet encryption and differential privacy noise.

    Notes:
    - If `cryptography` is available and an `encryption_key` is provided, Fernet is used.
    - Otherwise a base64 "encoding" is used as a non-secret fallback for demo / local use only.
    """

    def __init__(
        self,
        documents: List[str],
        embeddings: List[np.ndarray],
        encryption_key: Optional[str] = None,
        dp_epsilon: float = 1.0,
    ) -> None:
        self._use_fernet = bool(Fernet and encryption_key)
        # Avoid using Fernet in type annotation at runtime when package may be missing
        self._fernet_key = self._generate_key(encryption_key) if self._use_fernet else None
        self.documents = [self._encrypt(doc) for doc in documents]
        try:
            import numpy as np
        except Exception:
            np = None
            import random as _random
            import math as _math
        # Support running without numpy by storing embeddings as numpy array when
        # available or as a nested list otherwise.
        if np is not None:
            self.embeddings = np.array(embeddings, dtype=float)
        else:
            # Ensure numbers are floats
            self.embeddings = [list(map(float, e)) for e in embeddings]
        self.dp_epsilon = float(dp_epsilon) if dp_epsilon > 0 else 1.0

    def _generate_key(self, password: str) -> Optional[object]:
        try:
            # Fernet requires a 32 url-safe base64-encoded key
            raw = hashlib.sha256(password.encode()).digest()
            b64 = base64.urlsafe_b64encode(raw)
            return Fernet(b64)
        except Exception as e:
            logging.error(f"Failed to generate Fernet key: {e}")
            return None

    def _encrypt(self, text: str) -> str:
        if self._use_fernet and self._fernet_key:
            return self._fernet_key.encrypt(text.encode()).decode()
        # Non-secret fallback: base64 encode (NOT encryption)
        return base64.b64encode(text.encode()).decode()

    def _decrypt(self, enc_text: str) -> str:
        if self._use_fernet and self._fernet_key:
            try:
                return self._fernet_key.decrypt(enc_text.encode()).decode()
            except Exception:
                logging.warning("Failed to decrypt with Fernet; returning empty string")
                return ""
        try:
            return base64.b64decode(enc_text.encode()).decode()
        except Exception:
            logging.warning("Failed to base64-decode document; returning empty string")
            return ""

    def retrieve(self, query_embedding: np.ndarray, top_k: int = 3) -> List[str]:
        """Retrieve top_k documents by (unnormalized) dot product with optional Laplace DP noise.

        This implementation expects embeddings to be small arrays; for production use a vector DB is
        recommended.
        """
        # Normalize query embedding to a list/array of floats
        if np is not None:
            query_embedding = np.asarray(query_embedding, dtype=float)
            if query_embedding.shape != self.embeddings.shape[1:]:
                raise ValueError("Query embedding has incompatible shape")
            # Add Laplace noise for differential privacy (simple mechanism).
            scale = 1.0 / max(self.dp_epsilon, 1e-8)
            rng = np.random.default_rng()
            noise = rng.laplace(0.0, scale=scale, size=query_embedding.shape)
            noisy_query = query_embedding + noise

            similarities = np.dot(self.embeddings, noisy_query)
            # Guard against asking for more results than available
            k = max(1, min(int(top_k), len(self.documents)))
            top_indices = np.argsort(similarities)[-k:][::-1]
            return [self._decrypt(self.documents[int(i)]) for i in top_indices]
        else:
            # Pure-Python fallback when numpy not installed. No DP noise (or a
            # simple Laplace sampler) is applied to avoid heavy dependencies.
            q = [float(x) for x in query_embedding]
            dim = len(self.embeddings[0]) if self.embeddings else 0
            if len(q) != dim:
                raise ValueError("Query embedding has incompatible shape")

            # Laplace sampler
            def _laplace_sample(b: float) -> float:
                u = _random.random() - 0.5
                return -b * _math.copysign(_math.log(1 - 2 * abs(u)), u)

            scale = 1.0 / max(self.dp_epsilon, 1e-8)
            noisy_q = [qi + _laplace_sample(scale) for qi in q]

            def _dot(a, b):
                return sum(x * y for x, y in zip(a, b))

            similarities = [_dot(e, noisy_q) for e in self.embeddings]
            k = max(1, min(int(top_k), len(self.documents)))
            top_indices = sorted(range(len(similarities)), key=lambda i: similarities[i], reverse=True)[:k]
            return [self._decrypt(self.documents[int(i)]) for i in top_indices]

class PromptInjectionDetector:
    """Simple prompt-injection detector using regex patterns tuned for legal prompts."""

    def __init__(self) -> None:
        self.injection_patterns = [
            r"ignore.*previous.*instructions",
            r"you are now (?:a )?(?:hacker|attorney|disclose client)",
            r"system prompt:.*",
            r"forget.*rules|override|confidential",
            r"output .*json.*key=.*secret",
            r"reveal .*privileged|attorney-client",
        ]
        self.patterns = [re.compile(p, re.IGNORECASE) for p in self.injection_patterns]

    def detect(self, prompt: str) -> bool:
        prompt = prompt or ""
        for pattern in self.patterns:
            if pattern.search(prompt):
                logging.warning(f"Potential injection detected: {prompt[:200]}")
                return True
        return False

class SensitiveDataDetector:
    """Detects simple PII patterns (SSN, emails, case numbers, basic bar ids).

    This is a lightweight detector for demo purposes. Do not rely on it for
    production redaction without additional verification and human review.
    """

    def __init__(self) -> None:
        self.pii_patterns = [
            (r"\b\d{3}-\d{2}-\d{4}\b", "ssn"),
            (r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b", "email"),
            (r"\b\d{4}-\d{4}-\d{4}-\d{4}\b|\b\d{16}\b", "credit_card"),
            (r"\b[A-Z]{2,}-\d{4}-\d{4}\b", "case_id"),
            (r"\b\d{5,7}\b", "bar_number"),
            (r"\b(?:client|plaintiff|defendant):?\s*[A-Z][a-z]+\s[A-Z][a-z]+\b", "name"),
        ]
        self.patterns = [(re.compile(p, re.IGNORECASE), label) for p, label in self.pii_patterns]

    def detect(self, text: str) -> List[str]:
        text = text or ""
        matches = []
        for pattern, label in self.patterns:
            for m in pattern.findall(text):
                # pattern.findall may return tuple groups or strings
                if isinstance(m, tuple):
                    m = next((g for g in m if g), "")
                matches.append(m)
        if matches:
            logging.warning(f"Sensitive data found ({len(matches)} items)")
        # return unique matches
        return list(dict.fromkeys([m for m in matches if m]))

class LocalSummarizer:
    """Very small rule-based summarizer for demo/testing only."""

    def summarize(self, context: str, max_length: int = 200) -> str:
        context = context or ""
        # naive sentence split and return the first few sentences clipped to max_length
        sentences = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', context)
        summary = " ".join([s.strip() for s in sentences if s])[:max_length]
        if len(summary) == 0 and context:
            # fallback to truncation
            summary = context[:max_length]
        return summary + ("..." if len(summary) >= max_length else "")

class RAGSecureWrapper:
    """Strict, confidential wrapper for law-firm RAG operations."""

    def __init__(self, vector_store: EncryptedVectorStore, encryption_key: str, redact_sensitive: bool = True) -> None:
        self.vector_store = vector_store
        self.injection_detector = PromptInjectionDetector()
        self.sensitive_detector = SensitiveDataDetector()
        self.summarizer = LocalSummarizer()
        self.redact_sensitive = redact_sensitive
        self.encryption_key = encryption_key or ""

    def _validate_token(self, token: Optional[str], user_role: str) -> bool:
        # Simulate a minimal auth check using a hash; replace with real JWT in production.
        if not token:
            logging.error("Missing auth token")
            return False
        expected = hashlib.sha256((user_role + self.encryption_key).encode()).hexdigest()
        if token != expected:
            logging.error("Invalid auth token")
            return False
        return True

    def query(self, query: str, query_embedding: np.ndarray, user_role: str = "attorney", auth_token: Optional[str] = None) -> Dict[str, Any]:
        result: Dict[str, Any] = {"query": query, "role": user_role, "timestamp": datetime.now(timezone.utc).isoformat()}

        # 1. Strict Auth Check
        if not self._validate_token(auth_token, user_role):
            result["error"] = "Unauthorized access - invalid token"
            return result

        # 2. Prompt Injection Check
        if self.injection_detector.detect(query):
            result["error"] = "Prompt injection detected - query blocked"
            result["response"] = None
            return result

        # 3. Role Restrictions (e.g., paralegals can't access certain queries)
        if user_role not in ["attorney", "admin"]:
            result["error"] = "Insufficient role privileges"
            return result

        # 4. Secure Retrieval
        retrieved_docs = self.vector_store.retrieve(query_embedding, top_k=3)
        result["retrieved_docs"] = retrieved_docs  # decrypted (or base64-decoded) strings

        # 5. Sensitive Data Scan & Redaction
        all_sensitive: List[str] = []
        for i, doc in enumerate(retrieved_docs):
            sens = self.sensitive_detector.detect(doc)
            if sens:
                all_sensitive.extend(sens)
                if self.redact_sensitive:
                    retrieved_docs[i] = self._redact(doc, sens)

        if all_sensitive:
            result["warnings"] = {"sensitive_in_docs": all_sensitive}

        # 6. Local Generation (No external calls)
        context = " ".join(retrieved_docs)
        response = self.summarizer.summarize(context)

        # 7. Output Scan & Redaction
        sensitive_in_response = self.sensitive_detector.detect(response)
        if sensitive_in_response:
            result["warnings"] = {**result.get("warnings", {}), "sensitive_in_response": sensitive_in_response}
            if self.redact_sensitive:
                response = self._redact(response, sensitive_in_response)

        result["response"] = response
        return result

    def _redact(self, text: str, sensitive_items: List[str]) -> str:
        for item in sensitive_items:
            if not item:
                continue
            text = re.sub(re.escape(item), "[CONFIDENTIAL]", text, flags=re.IGNORECASE)
        return text

# Example Usage (Demo - Run on secure server)
if __name__ == "__main__":
    # Demo usage (keep this minimal and do not run on untrusted hosts)
    docs = [
        "Client: John Doe, Case: CV-1234-5678. Bar: 123456. Details: Confidential settlement.",
        "Neutral legal precedent on contracts.",
        "Plaintiff: Jane Smith, SSN: 123-45-6789. Email: jane@law.com.",
    ]
    embs = [[1.0, 0.1], [0.5, 0.8], [0.9, 0.6]]

    key = "lawfirm_secret_key_2025"
    evs = EncryptedVectorStore(docs, embs, encryption_key=key, dp_epsilon=0.5)
    secure_rag = RAGSecureWrapper(evs, encryption_key=key)

    q_emb = np.array([0.8, 0.5])
    auth_token = hashlib.sha256(("attorney" + key).encode()).hexdigest()

    print("Demo run: querying with valid auth token")
    print(secure_rag.query("Summarize case details", q_emb, user_role="attorney", auth_token=auth_token))