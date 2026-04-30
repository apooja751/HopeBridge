from pydantic import BaseModel
from typing import Optional

class OrphanageCreate(BaseModel):
    name: str
    address: Optional[str] = None
    city: Optional[str] = None
    contact: Optional[str] = None
    description: Optional[str] = None

class OrphanageResponse(BaseModel):
    orphanage_id: int
    name: str
    address: Optional[str]
    city: Optional[str]
    contact: Optional[str]
    description: Optional[str]

    class Config:
        from_attributes = True