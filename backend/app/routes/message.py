from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import models
from app.schemas.message_schema import MessageCreate, MessageResponse

router = APIRouter(prefix="/message", tags=["Message"])

@router.post("/send", response_model=MessageResponse)
def send_message(request: MessageCreate, db: Session = Depends(get_db)):
    new_message = models.Message(
        sender_id=request.sender_id,
        message=request.message
    )

    db.add(new_message)
    db.commit()
    db.refresh(new_message)

    return new_message

@router.get("/all", response_model=list[MessageResponse])
def get_messages(db: Session = Depends(get_db)):
    messages = db.query(models.Message).all()
    return messages