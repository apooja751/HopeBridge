<<<<<<< HEAD
from fastapi import APIRouter, Depends
from fastapi import HTTPException, Depends
=======
>>>>>>> dae0dc76075238ad0ffce9667fdc083ac91a9eb5
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime

from app.database import get_db
from fastapi import APIRouter
from app.models.models import Donation
from app.models import models
from app.models.models import Request
from app.schemas.donation_schema import DonationCreate, DonationResponse
from app.utils.dependencies import get_current_user

router = APIRouter(prefix="/donations", tags=["Donations"])


# ✅ CREATE DONATION
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
        pickup_date=donation.pickup_date,
        pickup_time=donation.pickup_time,
        pickup_address=donation.pickup_address,
        status="pending"
    )

    db.add(new_donation)
    db.commit()
    db.refresh(new_donation)

    return new_donation


# ✅ GET ALL DONATIONS
@router.get("/", response_model=list[DonationResponse])
def get_all_donations(db: Session = Depends(get_db)):
<<<<<<< HEAD
    donations = db.query(models.Donation).all()
    return donations

@router.put("/donations/{donation_id}")
def update_donation(donation_id: int, db: Session = Depends(get_db)):

    donation = db.query(Donation).filter(Donation.donation_id == donation_id).first()

    if donation is None:
        raise HTTPException(status_code=404, detail="Donation not found")

        # Step 3: Sync with request
    request = db.query(Request).filter(Request.request_id == donation.request_id).first()

    if request:
        request.status = "completed"
=======
    return db.query(models.Donation).all()


# ✅ UPDATE DONATION STATUS (STEP 16 SYNC)
@router.put("/{donation_id}")
def update_donation_status(
    donation_id: int,
    status: str,
    db: Session = Depends(get_db)
):
    donation = db.query(models.Donation).filter(
        models.Donation.donation_id == donation_id
    ).first()

    if not donation:
        raise HTTPException(status_code=404, detail="Donation not found")

    donation.status = status

    # 🔄 SYNC WITH REQUEST
    if status == "completed":
        request_obj = db.query(models.Request).filter(
            models.Request.request_id == donation.request_id
        ).first()

        if request_obj:
            request_obj.status = "completed"
>>>>>>> dae0dc76075238ad0ffce9667fdc083ac91a9eb5

    db.commit()
    db.refresh(donation)

<<<<<<< HEAD
    return donation
=======
    return {
        "message": "Donation updated",
        "donation_id": donation_id,
        "status": donation.status
    }


# ✅ STEP 21 — SCHEDULE PICKUP (FIXED)
@router.put("/{donation_id}/schedule")
def schedule_pickup(
    donation_id: int,
    pickup_date: str,
    pickup_time: str,
    pickup_address: str,
    db: Session = Depends(get_db)
):
    donation = db.query(models.Donation).filter(
        models.Donation.donation_id == donation_id
    ).first()

    if not donation:
        raise HTTPException(status_code=404, detail="Donation not found")

    # 🔄 Convert string → datetime
    try:
        pickup_date_obj = datetime.fromisoformat(pickup_date)
    except:
        raise HTTPException(status_code=400, detail="Invalid date format")

    # ✅ Validate future date
    if pickup_date_obj <= datetime.now():
        raise HTTPException(
            status_code=400,
            detail="Pickup date must be in the future"
        )

    # ✅ Required fields
    if not pickup_time or not pickup_address:
        raise HTTPException(
            status_code=400,
            detail="Pickup time and address are required"
        )

    # ✅ Update
    donation.pickup_date = pickup_date_obj
    donation.pickup_time = pickup_time
    donation.pickup_address = pickup_address

    db.commit()
    db.refresh(donation)

    return {
        "message": "Pickup scheduled successfully",
        "donation_id": donation_id
    }
>>>>>>> dae0dc76075238ad0ffce9667fdc083ac91a9eb5
