from pydantic import BaseModel

class DonationStatusUpdate(BaseModel):
    donation_id: int
    status: str

class DeliveryStatusUpdate(BaseModel):
    donation_id: int
    delivery_status: str

class RequestStatusUpdate(BaseModel):
    request_id: int
    status: str