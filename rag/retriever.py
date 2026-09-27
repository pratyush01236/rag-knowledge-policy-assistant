import re
from .models import RetrievalResult
from .policy import question_date,latest_applicable
from .security import contains_injection

class Retriever:
    def __init__(self,documents): self.documents=documents

    def retrieve(self,question,user,today=None,top_k=5):
        from datetime import date
        target=question_date(question) if re.search(r'20\\d{2}-\\d{2}-\\d{2}',question) else (today or date.today())
        allowed=[d for d in self.documents if user.can_access(d) and d.is_active(target) and not contains_injection(d.content)]
        policies=[d for d in allowed if 'policy' in d.title.lower()]
        nonpol=[d for d in allowed if d not in policies]
        chosen={}
        for d in policies:
            key=(d.product,d.region)
            old=chosen.get(key)
            if old is None or (d.effective_date,d.version)>(old.effective_date,old.version): chosen[key]=d
        candidates=nonpol+list(chosen.values())
        q=set(re.findall(r'[a-z0-9]+',question.lower()))
        scored=[]
        for d in candidates:
            words=set(re.findall(r'[a-z0-9]+',(d.title+' '+d.content).lower()))
            scored.append((len(q & words),d))
        scored=sorted(scored,key=lambda x:x[0],reverse=True)[:top_k]
        return [RetrievalResult(d,float(score),f'[{d.document_id} v{d.version}; effective {d.effective_date}; region {d.region}]') for score,d in scored if score>0]
