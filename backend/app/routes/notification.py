from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import models
from app.schemas.notification_schema import NotificationCreate, NotificationResponse

router = APIRouter(prefix="/notification", tags=["Notification"])


@router.post("/create", response_model=NotificationResponse)
def create_notification(request: NotificationCreate, db: Session = Depends(get_db)):
    new_notification = models.Notification(
        user_id=request.user_id,
        message=request.message,
        is_read=False
    )

    db.add(new_notification)
    db.commit()
    db.refresh(new_notification)

    return new_notification


@router.get("/user/{user_id}", response_model=list[NotificationResponse])
def get_notifications(user_id: int, db: Session = Depends(get_db)):
    return db.query(models.Notification).filter(models.Notification.user_id == user_id).all()