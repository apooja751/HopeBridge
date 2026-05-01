from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import models

from app.utils.dependencies import require_role
from app.schemas.admin_schema import (
    UserResponse,
    OrphanageVerify,
    RequestStatusUpdate,
    DonationStatusUpdate
)

router = APIRouter(prefix="/admin", tags=["Admin"])


# 🔹 View all users
@router.get("/users", response_model=list[UserResponse], dependencies=[Depends(require_role("admin"))])
def get_all_users(db: Session = Depends(get_db)):
    users = db.query(models.User).all()
    return users


# 🔹 Verify orphanage
@router.put("/verify-orphanage", dependencies=[Depends(require_role("admin"))])
def verify_orphanage(data: OrphanageVerify, db: Session = Depends(get_db)):
    orphanage = db.query(models.Orphanage).filter(
        models.Orphanage.orphanage_id == data.orphanage_id
    ).first()

    if orphanage:
        orphanage.is_verified = data.is_verified
        db.commit()
        return {"message": "Orphanage verification updated"}

    return {"message": "Orphanage not found"}


# 🔹 Update request status
@router.put("/request-status", dependencies=[Depends(require_role("admin"))])
def update_request_status(data: RequestStatusUpdate, db: Session = Depends(get_db)):
    request = db.query(models.Request).filter(
        models.Request.request_id == data.request_id
    ).first()

    if request:
        request.status = data.status
        db.commit()
        return {"message": "Request status updated"}

    return {"message": "Request not found"}


# 🔹 Update donation status
@router.put("/donation-status", dependencies=[Depends(require_role("admin"))])
def update_donation_status(data: DonationStatusUpdate, db: Session = Depends(get_db)):
    donation = db.query(models.Donation).filter(
        models.Donation.donation_id == data.donation_id
    ).first()

    if donation:
        donation.status = data.status
        db.commit()
        return {"message": "Donation status updated"}

    return {"message": "Donation not found"}