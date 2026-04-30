from pydantic import BaseModel

class NotificationCreate(BaseModel):
    user_id: int
    message: str

class NotificationResponse(BaseModel):
    notification_id: int
    user_id: int
    message: str
    is_read: bool

    class Config:
        from_attributes = True