from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import models
from app.utils.dependencies import require_role

router = APIRouter(prefix="/donor", tags=["Donor"])


# Get all requests (Public - no role restriction)
@router.get("/requests")
def get_all_requests(db: Session = Depends(get_db)):
    return db.query(models.Request).all()


# Create Donation (Only donor role)
@router.post("/donate")
def create_donation(
    user_id: int,
    request_id: int,
    donation_type: str,
    amount: float = None,
    items_description: str = None,
    quantity: int = None,
    db: Session = Depends(get_db),
    user=Depends(require_role("donor"))
):
    donation = models.Donation(
        user_id=user_id,
        request_id=request_id,
        donation_type=donation_type,
        amount=amount,
        items_description=items_description,
        quantity=quantity
    )
    
    db.add(donation)
    db.commit()
    db.refresh(donation)
    
    return {"message": "Donation created successfully"}


# Get my donations (Only donor role)
@router.get("/my-donations")
def get_my_donations(
    user_id: int,
    db: Session = Depends(get_db),
    user=Depends(require_role("donor"))
):
    return db.query(models.Donation).filter(
        models.Donation.user_id == user_id
    ).all()