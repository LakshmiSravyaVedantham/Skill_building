# Security — RAG security demo

This repository contains a small demo showing hardened local checks for RAG (Retrieval-Augmented Generation) in a legal context. It is intended for demonstration and testing only.

Quick start

1. Create a virtual environment and activate it:

```bash
python -m venv .venv
source .venv/bin/activate
```

2. Install dependencies:

```bash
python -m pip install -r requirements.txt
```

3. Run tests:

```bash
python -m pytest -q
```

Usage (demo)

See `main.py` for a minimal example. In short, create an `EncryptedVectorStore`, wrap it with `RAGSecureWrapper`, and call `query()` with a valid auth token (the tests show a small example).

CI

This repository includes a GitHub Actions workflow at `.github/workflows/ci.yml` that runs the test suite for pull requests and pushes.

Important notes

- The `cryptography` package is optional for demo runs; the code will fallback to base64 encoding when unavailable — this is NOT secure and only for local testing.
- Do not use this code as-is in production for handling real PII or client data without additional safeguards and legal review.

Contributing

1. Create a branch for your change: `git checkout -b feature/your-change`
2. Run tests: `python -m pytest -q`
3. Commit and push to a branch and open a pull request.

Contact

For questions about this demo, open an issue in the repository.
