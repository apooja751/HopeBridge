from pydantic import BaseModel

class InquiryCreate(BaseModel):
    user_id: int
    message: str

class InquiryResponse(BaseModel):
    inquiry_id: int
    user_id: int
    message: str

    class Config:
        from_attributes = True
        