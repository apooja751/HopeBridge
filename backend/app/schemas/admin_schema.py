from pydantic import BaseModel
from typing import Optional
from enum import Enum

class UserResponse(BaseModel):
    user_id: int
    name: str
    email: str
    role: str

    class Config:
        from_attributes = True


class OrphanageVerify(BaseModel):
    orphanage_id: int
    is_verified: bool

class RequestStatusEnum(str, Enum):
    pending = "pending"
    approved = "approved"
    rejected = "rejected"
    in_progress = "in_progress"

class RequestStatusUpdate(BaseModel):
    request_id: int
    status: RequestStatusEnum


class RequestStatusEnum(str, Enum):
    active = "active"
    fulfilled = "fulfilled"

class RequestStatusUpdate(BaseModel):
    request_id: int
    status: RequestStatusEnum

class DonationStatusUpdate(BaseModel):
    donation_id: int
    status: str