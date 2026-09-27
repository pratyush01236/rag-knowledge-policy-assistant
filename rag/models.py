from dataclasses import dataclass
from datetime import date

ACCESS_ORDER={'public':0,'customer':1,'internal':2,'restricted':3}

@dataclass(frozen=True)
class Document:
    document_id:str
    version:str
    product:str
    region:str
    access_level:str
    effective_date:date
    expiry_date:date|None
    title:str
    content:str

    def is_active(self,on_date:date)->bool:
        return self.effective_date<=on_date and (self.expiry_date is None or on_date<=self.expiry_date)

@dataclass(frozen=True)
class UserContext:
    access_level:str
    region:str
    products:tuple[str,...]=()

    def can_access(self,doc:Document)->bool:
        return ACCESS_ORDER.get(self.access_level,-1)>=ACCESS_ORDER.get(doc.access_level,99) and (doc.region=='GLOBAL' or doc.region==self.region) and (not self.products or doc.product in self.products or doc.product=='GLOBAL')
