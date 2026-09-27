# RAG Knowledge Policy Assistant

Security-aware RAG assistant for product documents, FAQs, policies and troubleshooting guides.

## Features
- Version, product, region, access level, effective date and expiry date metadata.
- Authorization filtering before retrieval.
- Current questions ignore future and expired documents.
- Historical questions retrieve documents active on the requested date.
- Conflicting policies select the latest applicable version.
- Factual retrieval results always carry source citations.
- Missing evidence returns a refusal rather than an invented answer.
- Documents are treated as untrusted data; embedded instructions are filtered.
- Tests cover conflicting, restricted, future, historical and injected documents.

## Run
```bash
python -m venv venv
# Windows
venv\\Scripts\\activate
pip install -r requirements.txt
pytest -q
python app.py
```

## Example
Current: `What is the refund policy for Product X?`

Historical: `What was the refund policy on 2025-06-01?`

## Architecture
`documents -> authorization/date filtering -> policy conflict resolution -> retrieval -> cited answer/refusal`

This is a reference implementation. A production deployment should connect access checks to a real identity provider and replace the simple lexical retriever with a persistent vector database.
