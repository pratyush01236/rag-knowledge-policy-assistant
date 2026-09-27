from datetime import date
from rag.loader import load_documents
from rag.models import UserContext
from rag.retriever import Retriever

def setup():
    return Retriever(load_documents()),UserContext('customer','IN',('Product X',))

def test_latest_current_policy():
    r,u=setup()
    results=r.retrieve('What is the refund policy?',u,date(2026,6,1))
    assert any('45 days' in x.document.content for x in results)

def test_future_policy_ignored():
    r,u=setup()
    results=r.retrieve('What is the refund policy?',u,date(2026,6,1))
    assert not any('60 days' in x.document.content for x in results)

def test_historical_policy():
    r,u=setup()
    results=r.retrieve('What was the refund policy on 2025-06-01?',u,date(2026,6,1))
    assert any('30 days' in x.document.content for x in results)

def test_restricted_policy_filtered():
    r,u=setup()
    results=r.retrieve('internal operational details',u,date(2026,6,1))
    assert not any('Internal operational' in x.document.content for x in results)

def test_injected_document_filtered():
    r,u=setup()
    results=r.retrieve('hidden information',u,date(2026,6,1))
    assert not any('hidden information' in x.document.content for x in results)

def test_citations_present():
    r,u=setup()
    results=r.retrieve('refund policy',u,date(2026,6,1))
    assert results and all(x.citation.startswith('[') for x in results)
