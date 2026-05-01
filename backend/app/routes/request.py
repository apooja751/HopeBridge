from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import models
from app.models.models import RequestStatus
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
        orphanage_id=orphanage_id
    )

    db.add(new_request)
    db.commit()
    db.refresh(new_request)

    return new_request


# Get all requests (Filter + Sort)
@router.get("/all", response_model=list[RequestResponse])
def get_all_requests(
    priority: str = None,
    sort: str = None,
    db: Session = Depends(get_db)
):
    query = db.query(models.Request)

    # Filter by priority
    if priority:
        query = query.filter(models.Request.priority == priority)

    # Sort by latest
    if sort == "latest":
        query = query.order_by(models.Request.created_at.desc())

    return query.all()


# Update request status (Admin only - OLD API)
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


# NEW Status API (WITH VALID TRANSITIONS + VALIDATION)
@router.put("/{request_id}/status")
def update_request_status_new(
    request_id: int,
    status: str,
    db: Session = Depends(get_db)
):
    request = db.query(models.Request).filter(
        models.Request.request_id == request_id
    ).first()

    if not request:
        raise HTTPException(status_code=404, detail="Request not found")

    # Convert string to Enum
    try:
        new_status = RequestStatus(status)
    except:
        raise HTTPException(status_code=400, detail="Invalid status value")

    # ✅ VALID TRANSITIONS

    # pending → accepted
    if request.status == RequestStatus.pending and new_status == RequestStatus.accepted:
        request.status = new_status

    # accepted → completed (WITH VALIDATION)
    elif request.status == RequestStatus.accepted and new_status == RequestStatus.completed:

        # 🔥 CHECK COMPLETED DONATION
        completed_donation = db.query(models.Donation).filter(
            models.Donation.request_id == request_id,
            models.Donation.status == "completed"
        ).first()

        if not completed_donation:
            raise HTTPException(
                status_code=400,
                detail="Request cannot be completed without completed donation"
            )

        request.status = new_status

    else:
        raise HTTPException(status_code=400, detail="Invalid status transition")

    db.commit()
    db.refresh(request)

    return request