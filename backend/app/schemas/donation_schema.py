from pydantic import BaseModel
from typing import Optional
from enum import Enum

class DonationType(str, Enum):
    item = "item"
    money = "money"

class DonationCreate(BaseModel):
    request_id: int
    donation_type: DonationType
    amount: Optional[float] = None
    items_description: Optional[str] = None
    quantity: Optional[int] = None

class DonationResponse(BaseModel):
    donation_id: int
    request_id: int
    donation_type: str
    amount: Optional[float]
    items_description: Optional[str]
    quantity: Optional[int]
    status: str

    class Config:
        from_attributes = True