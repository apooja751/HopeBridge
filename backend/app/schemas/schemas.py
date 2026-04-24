from pydantic import BaseModel
from typing import Optional
from enum import Enum

class UserRole(str, Enum):
    donor = "donor"
    orphanage = "orphanage"
    admin = "admin"

# ── Auth Schemas ───────────────────────────────────
class RegisterRequest(BaseModel):
    name: str
    email: str
    password: str
    phone: Optional[str] = None
    role: UserRole

class LoginRequest(BaseModel):
    email: str
    password: str

class TokenResponse(BaseModel):
    access_token: str
    token_type: str
    role: str
    user_id: int
    name: str