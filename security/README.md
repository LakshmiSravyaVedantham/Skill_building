# ETL_SQL - RAG Secure Demo

This small demo contains a minimal RAG-like wrapper focused on local security checks for legal contexts.

Files added/modified:

How to run tests:

```bash
python -m pip install -r requirements.txt
pytest -q
```

Notes:
Usage (demo):

```python
from main import EncryptedVectorStore, RAGSecureWrapper
import numpy as np, hashlib

docs = ["Client: John Doe.", "Neutral note."]
embs = [[1.0, 0.0], [0.0, 1.0]]
key = "lawfirm_secret_key"
evs = EncryptedVectorStore(docs, embs, encryption_key=key)
wrapper = RAGSecureWrapper(evs, encryption_key=key)
q_emb = np.array([1.0, 0.0])
token = hashlib.sha256(("attorney" + key).encode()).hexdigest()
print(wrapper.query("Summarize", q_emb, user_role="attorney", auth_token=token))
```

CI

This repository includes a GitHub Actions workflow that runs tests on push and pull requests. After the workflow runs you will see test results in the Checks tab.
