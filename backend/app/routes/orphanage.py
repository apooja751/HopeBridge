from app.utils.dependencies import require_role
from fastapi import APIRouter, Depends, Body, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.orphanage_schema import OrphanageCreate, OrphanageResponse
from app.models import models

router = APIRouter(prefix="/orphanage", tags=["Orphanage"])


# Create Orphanage (Only orphanage role)
@router.post("/create", response_model=OrphanageResponse)
def create_orphanage(
    request: OrphanageCreate,
    db: Session = Depends(get_db),
    user=Depends(require_role("orphanage"))
):
    new_orphanage = models.Orphanage(
        name=request.name,
        address=request.address,
        city=request.city,
        contact=request.contact,
        description=request.description
    )

    db.add(new_orphanage)
    db.commit()
    db.refresh(new_orphanage)

    return new_orphanage


# Get All Orphanages (Public)
@router.get("/all", response_model=list[OrphanageResponse])
def get_all_orphanages(db: Session = Depends(get_db)):
    return db.query(models.Orphanage).all()


# Update Orphanage (Only orphanage role)
@router.put("/update/{orphanage_id}", response_model=OrphanageResponse)
def update_orphanage(
    orphanage_id: int,
    request: OrphanageCreate = Body(...),
    db: Session = Depends(get_db),
    user=Depends(require_role("orphanage"))
):
    orphanage = db.query(models.Orphanage).filter(
        models.Orphanage.orphanage_id == orphanage_id
    ).first()

    if not orphanage:
        raise HTTPException(status_code=404, detail="Orphanage not found")

    orphanage.name = request.name
    orphanage.address = request.address
    orphanage.city = request.city
    orphanage.contact = request.contact
    orphanage.description = request.description

    db.commit()
    db.refresh(orphanage)

    return orphanage


# Delete Orphanage (Only orphanage role)
@router.delete("/delete/{orphanage_id}")
def delete_orphanage(
    orphanage_id: int,
    db: Session = Depends(get_db),
    user=Depends(require_role("orphanage"))
):
    orphanage = db.query(models.Orphanage).filter(
        models.Orphanage.orphanage_id == orphanage_id
    ).first()

    if not orphanage:
        raise HTTPException(status_code=404, detail="Orphanage not found")

    db.delete(orphanage)
    db.commit()

    return {"message": "Orphanage deleted successfully"}