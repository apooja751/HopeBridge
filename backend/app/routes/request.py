from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import models
from app.models.models import RequestStatus
from app.schemas.request_schema import RequestCreate, RequestResponse
from app.utils.dependencies import require_role, get_current_user

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


# ✅ STEP 19 — Pagination + Filter + Sort + Role-Based (FINAL CLEAN)
@router.get("/all")
def get_all_requests(
    page: int = 1,
    limit: int = 10,
    priority: str = None,
    sort: str = None,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    query = db.query(models.Request)

    role = user.get("role")

    # Role-based filtering
    if role == "orphanage":
        orphanage_id = user.get("user_id")
        query = query.filter(models.Request.orphanage_id == orphanage_id)

    # Donor → all
    elif role == "donor":
        pass

    # Admin → all
    elif role == "admin":
        pass

    # Filtering
    if priority:
        query = query.filter(models.Request.priority == priority)

    # Sorting
    if sort == "latest":
        query = query.order_by(models.Request.created_at.desc())

    # Total count
    total = query.count()

    # Pagination
    skip = (page - 1) * limit
    results = query.offset(skip).limit(limit).all()

    # Clean response (safe serialization)
    data = []
    for r in results:
        data.append({
            "request_id": r.request_id,
            "title": r.title,
            "category": r.category,
            "description": r.description,
            "priority": r.priority,
            "status": r.status,
            "orphanage_id": r.orphanage_id,
            "created_at": r.created_at
        })

    return {
        "total": total,
        "page": page,
        "limit": limit,
        "data": data
    }


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


# Status API (Step 15 + 17)
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

    try:
        new_status = RequestStatus(status)
    except:
        raise HTTPException(status_code=400, detail="Invalid status value")

    # pending → accepted
    if request.status == RequestStatus.pending and new_status == RequestStatus.accepted:
        request.status = new_status

    # accepted → completed (with validation)
    elif request.status == RequestStatus.accepted and new_status == RequestStatus.completed:

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