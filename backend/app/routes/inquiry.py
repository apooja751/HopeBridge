from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import models
from app.schemas.inquiry_schema import InquiryCreate, InquiryResponse

router = APIRouter(prefix="/inquiry", tags=["Inquiry"])

@router.post("/create", response_model=InquiryResponse)
def create_inquiry(request: InquiryCreate, db: Session = Depends(get_db)):
    new_inquiry = models.Message(   # reuse Message table (no new model needed)
        sender_id=request.user_id,
        message=request.message
    )

    db.add(new_inquiry)
    db.commit()
    db.refresh(new_inquiry)

    return {
        "inquiry_id": new_inquiry.message_id,
        "user_id": new_inquiry.sender_id,
        "message": new_inquiry.message
    }