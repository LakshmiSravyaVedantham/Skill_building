import numpy as np
from main import EncryptedVectorStore, RAGSecureWrapper
import hashlib


def test_encrypted_vector_store_basic():
    docs = ["A one.", "B two.", "C three."]
    embs = [[1.0, 0.0], [0.0, 1.0], [0.5, 0.5]]
    evs = EncryptedVectorStore(docs, embs, encryption_key=None, dp_epsilon=1.0)
    q = np.array([1.0, 0.0])
    res = evs.retrieve(q, top_k=1)
    assert isinstance(res, list) and len(res) == 1


def test_rag_secure_wrapper_auth_and_retrieval():
    docs = ["Client: John Doe.", "Neutral note."]
    embs = [[1.0, 0.0], [0.0, 1.0]]
    key = "k"
    evs = EncryptedVectorStore(docs, embs, encryption_key=key, dp_epsilon=1.0)
    wrapper = RAGSecureWrapper(evs, encryption_key=key)
    q_emb = np.array([1.0, 0.0])
    token = hashlib.sha256(("attorney" + key).encode()).hexdigest()
    out = wrapper.query("Summarize", q_emb, user_role="attorney", auth_token=token)
    assert "response" in out
