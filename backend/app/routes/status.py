from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import models
from app.schemas.status_schema import (
    DonationStatusUpdate,
    DeliveryStatusUpdate,
    RequestStatusUpdate
)

router = APIRouter(prefix="/status", tags=["Status"])


# 🔹 Update donation status
@router.put("/donation")
def update_donation_status(data: DonationStatusUpdate, db: Session = Depends(get_db)):
    donation = db.query(models.Donation).filter(
        models.Donation.donation_id == data.donation_id
    ).first()

    if donation:
        donation.status = data.status
        db.commit()
        return {"message": "Donation status updated"}

    return {"message": "Donation not found"}


# 🔹 Update delivery status
@router.put("/delivery")
def update_delivery_status(data: DeliveryStatusUpdate, db: Session = Depends(get_db)):
    donation = db.query(models.Donation).filter(
        models.Donation.donation_id == data.donation_id
    ).first()

    if donation:
        donation.delivery_status = data.delivery_status
        db.commit()
        return {"message": "Delivery status updated"}

    return {"message": "Donation not found"}


# 🔹 Update request status
@router.put("/request")
def update_request_status(data: RequestStatusUpdate, db: Session = Depends(get_db)):
    request = db.query(models.Request).filter(
        models.Request.request_id == data.request_id
    ).first()

    if request:
        request.status = data.status
        db.commit()
        return {"message": "Request status updated"}

    return {"message": "Request not found"}