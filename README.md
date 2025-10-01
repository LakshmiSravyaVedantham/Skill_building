# Amazon ETL with Neon Database

This project contains a comprehensive ETL pipeline for processing **Amazon product data** and **NYC taxi trip data**, storing them in Neon Database (serverless PostgreSQL) with Grafana visualization.

## 📊 **[📈 Comprehensive Data Analysis →](DATA_ANALYSIS_README.md)**
*For detailed insights, business intelligence, and data patterns analysis*

## Prerequisites

- Docker Desktop installed and running
- Docker Compose installed

## Project Structure

```
Amazon/
├── data/
│   └── amazon.csv          # Input CSV data
├── etl/
│   └── extract_transform.py # ETL script
├── db/                     # Database initialization scripts
├── grafana/               # Grafana configuration
├── Dockerfile             # Docker image definition
├── docker-compose.yml     # Multi-container setup
├── requirements.txt       # Python dependencies
├── .env                   # Environment variables
└── README.md             # This file
```

## Quick Start

1. **Start Docker Desktop**
   ```bash
   open -a Docker  # On macOS
   ```

2. **Build and run the containers**
   ```bash
   docker-compose up --build
   ```

3. **Access services**
   - Neon Database: Serverless PostgreSQL (automatically managed)
   - Grafana: `http://localhost:3001`

4. **Run individual ETL processes**
   ```bash
   # Run Amazon product ETL
   ./run.sh etl

   # Run NYC Taxi ETL (Docker)
   ./run.sh nyc

   # Run NYC Taxi ETL (directly on host)
   ./run.sh nyc-local
   ```

## Manual Steps

### 1. Build the Docker image
```bash
docker build -t amazon-etl .
```
#!/usr/bin/env bash

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
   - Try running with `sudo` if on Linux
