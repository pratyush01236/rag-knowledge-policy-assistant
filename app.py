from datetime import date
from rag.loader import load_documents
from rag.models import UserContext
from rag.retriever import Retriever
from rag.answerer import answer

def main():
    retriever=Retriever(load_documents())
    user=UserContext('customer','IN',('Product X',))
    print('RAG Knowledge Policy Assistant')
    print('Ask a question or type exit.')
    while True:
        q=input('You: ').strip()
        if q.lower()=='exit': break
        print('Assistant:',answer(q,retriever,user,date.today()))

if __name__=='__main__':
    main()
