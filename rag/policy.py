import re
from datetime import date

def question_date(question):
    m=re.search(r'20\\d{2}-\\d{2}-\\d{2}',question)
    return date.fromisoformat(m.group()) if m else date.today()

def version_key(version):
    return tuple(int(x) for x in re.findall(r'\\d+',version)) or (0,)

def latest_applicable(docs,product,region,on_date):
    candidates=[d for d in docs if d.product in (product,'GLOBAL') and d.region in (region,'GLOBAL') and d.is_active(on_date)]
    return max(candidates,key=lambda d:(d.effective_date,version_key(d.version)),default=None)
