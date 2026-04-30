from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import models
from app.schemas.donation_schema import DonationCreate, DonationResponse

router = APIRouter(prefix="/donations", tags=["Donations"])

@router.post("/", response_model=DonationResponse)
def create_donation(donation: DonationCreate, db: Session = Depends(get_db)):
    new_donation = models.Donation(
    user_id=1,   # temporary (hardcoded)
    request_id=donation.request_id,
    donation_type=donation.donation_type,
    amount=donation.amount,
    items_description=donation.items_description,
    quantity=donation.quantity,
    status="pending"
    )

    db.add(new_donation)
    db.commit()
    db.refresh(new_donation)

    return new_donation

@router.get("/", response_model=list[DonationResponse])
def get_all_donations(db: Session = Depends(get_db)):
    donations = db.query(models.Donation).all()
    return donations