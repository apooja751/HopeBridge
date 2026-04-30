from pydantic import BaseModel
from typing import Optional
from enum import Enum

class RequestCategory(str, Enum):
    food = "food"
    clothes = "clothes"
    education = "education"
    medical = "medical"
    others = "others"

class RequestPriority(str, Enum):
    low = "low"
    medium = "medium"
    urgent = "urgent"

class RequestCreate(BaseModel):
    title: str
    category: RequestCategory
    description: Optional[str] = None
    priority: RequestPriority = RequestPriority.medium

class RequestResponse(BaseModel):
    request_id: int
    title: str
    category: RequestCategory
    description: Optional[str]
    priority: RequestPriority
    status: str

    class Config:
        from_attributes = True