from pydantic import BaseModel
from typing import Optional
from enum import Enum


# ── Enums ─────────────────────────────
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


# ── Create Schema ─────────────────────
class RequestCreate(BaseModel):
    title: str
    category: RequestCategory
    description: Optional[str] = None
    priority: RequestPriority   # ✅ FIXED (use Enum)


# ── Response Schema ───────────────────
class RequestResponse(BaseModel):
    request_id: int
    title: str
    category: RequestCategory
    description: Optional[str]
    priority: RequestPriority   # ✅ FIXED (use Enum)
    status: str                 # ✅ required for Step 15
    orphanage_id: int           # ✅ add this (important)

    class Config:
        from_attributes = True