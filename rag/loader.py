import json
from datetime import date
from pathlib import Path
from .models import Document

def load_documents(path='data/documents.json'):
    raw=json.loads(Path(path).read_text(encoding='utf-8'))
    return [Document(x['document_id'],x['version'],x['product'],x['region'],x['access_level'],date.fromisoformat(x['effective_date']),date.fromisoformat(x['expiry_date']) if x.get('expiry_date') else None,x['title'],x['content']) for x in raw]
