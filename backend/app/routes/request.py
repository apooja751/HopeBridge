from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import models
from app.schemas.request_schema import RequestCreate, RequestResponse

router = APIRouter(prefix="/request", tags=["Request"])

@router.post("/create", response_model=RequestResponse)
def create_request(request: RequestCreate, orphanage_id: int, db: Session = Depends(get_db)):
    new_request = models.Request(
        title=request.title,
        category=request.category,
        description=request.description,
        priority=request.priority,
        status="active",
        orphanage_id=orphanage_id
    )

    db.add(new_request)
    db.commit()
    db.refresh(new_request)

    return new_request

@router.get("/all", response_model=list[RequestResponse])
def get_all_requests(db: Session = Depends(get_db)):
    requests = db.query(models.Request).all()
    return requests

@router.get("/orphanage/{orphanage_id}", response_model=list[RequestResponse])
def get_requests_by_orphanage(orphanage_id: int, db: Session = Depends(get_db)):
    requests = db.query(models.Request).filter(models.Request.orphanage_id == orphanage_id).all()
    return requests

@router.put("/update-status/{request_id}")
def update_request_status(request_id: int, status: str, db: Session = Depends(get_db)):
    request = db.query(models.Request).filter(models.Request.request_id == request_id).first()
    
    if not request:
        return {"error": "Request not found"}
    
    request.status = status
    db.commit()
    db.refresh(request)

    return request