from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import models
from app.schemas.request_schema import RequestCreate, RequestResponse
from app.utils.dependencies import require_role

router = APIRouter(prefix="/request", tags=["Request"])


# Create Request (Only orphanage role)
@router.post("/create", response_model=RequestResponse)
def create_request(
    request: RequestCreate,
    orphanage_id: int,
    db: Session = Depends(get_db),
    user=Depends(require_role("orphanage"))
):
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


# Get all requests (Public)
@router.get("/all", response_model=list[RequestResponse])
def get_all_requests(db: Session = Depends(get_db)):
    return db.query(models.Request).all()


# Get requests by orphanage (Public)
@router.get("/orphanage/{orphanage_id}", response_model=list[RequestResponse])
def get_requests_by_orphanage(orphanage_id: int, db: Session = Depends(get_db)):
    return db.query(models.Request).filter(
        models.Request.orphanage_id == orphanage_id
    ).all()


# Update request status (Admin only)
@router.put("/update-status/{request_id}")
def update_request_status(
    request_id: int,
    status: str,
    db: Session = Depends(get_db),
    user=Depends(require_role("admin"))
):
    request = db.query(models.Request).filter(
        models.Request.request_id == request_id
    ).first()

    if not request:
        raise HTTPException(status_code=404, detail="Request not found")

    request.status = status
    db.commit()
    db.refresh(request)

    return request