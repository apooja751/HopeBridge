from pydantic import BaseModel

class MessageCreate(BaseModel):
    sender_id: int
    message: str

class MessageResponse(BaseModel):
    message_id: int
    sender_id: int
    message: str

    class Config:
        from_attributes = True