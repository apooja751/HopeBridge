
from fastapi import APIRouter, Depends
from fastapi import HTTPException, Depends

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime, timezone

from app.database import get_db
from fastapi import APIRouter
from app.models.models import Donation
from app.models import models
from app.models.models import Request
from app.schemas.donation_schema import DonationCreate, DonationResponse
from app.utils.dependencies import get_current_user

router = APIRouter(prefix="/donations", tags=["Donations"])


# CREATE DONATION
@router.post("/", response_model=DonationResponse)
def create_donation(
    donation: DonationCreate,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    new_donation = models.Donation(
        user_id=user.get("user_id"),
        request_id=donation.request_id,
        donation_type=donation.donation_type,
        amount=donation.amount,
        items_description=donation.items_description,
        quantity=donation.quantity,

        #  PICKUP FIELDS
        pickup_date=donation.pickup_date,
        pickup_time=donation.pickup_time,
        pickup_address=donation.pickup_address,

        status="pending"
    )

    db.add(new_donation)
    db.commit()
    db.refresh(new_donation)

    return new_donation


#  GET ALL DONATIONS
@router.get("/", response_model=list[DonationResponse])
def get_all_donations(db: Session = Depends(get_db)):
    donations = db.query(models.Donation).all()
    return donations

#  SCHEDULE PICKUP
@router.put("/{donation_id}/schedule")
def schedule_pickup(
    donation_id: int,
    pickup_date: datetime,
    pickup_time: str,
    pickup_address: str,
    db: Session = Depends(get_db)
):
    donation = db.query(models.Donation).filter(
        models.Donation.donation_id == donation_id
    ).first()

    if not donation:
        raise HTTPException(status_code=404, detail="Donation not found")

    # ✅ VALIDATION: pickup date required
    if pickup_date is None:
        raise HTTPException(
            status_code=400,
            detail="Pickup date required"
        )

    #  VALIDATION: must be future date
    if pickup_date <= datetime.now(timezone.utc):
        raise HTTPException(
            status_code=400,
            detail="Pickup date must be in the future"
        )

    # VALIDATION: required fields
    if not pickup_time or not pickup_address:
        raise HTTPException(
            status_code=400,
            detail="Pickup time and address are required"
        )

    #  UPDATE
    donation.pickup_date = pickup_date
    donation.pickup_time = pickup_time
    donation.pickup_address = pickup_address
@router.put("/donations/{donation_id}")
def update_donation(donation_id: int, db: Session = Depends(get_db)):

    donation = db.query(Donation).filter(Donation.donation_id == donation_id).first()

    if donation is None:
        raise HTTPException(status_code=404, detail="Donation not found")

        # Step 3: Sync with request
    request = db.query(Request).filter(Request.request_id == donation.request_id).first()

    if request:
        request.status = "completed"

    db.commit()
    db.refresh(donation)
    return {
        "message": "Pickup scheduled successfully",
        "donation_id": donation_id
    }
    return donation
