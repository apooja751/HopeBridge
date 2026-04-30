from fastapi import APIRouter, Depends, Body
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.orphanage_schema import OrphanageCreate, OrphanageResponse
from app.models import models

router = APIRouter(prefix="/orphanage", tags=["Orphanage"])

# Create Orphanage
@router.post("/create", response_model=OrphanageResponse)
def create_orphanage(request: OrphanageCreate, db: Session = Depends(get_db)):
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


# Get All Orphanages
@router.get("/all", response_model=list[OrphanageResponse])
def get_all_orphanages(db: Session = Depends(get_db)):
    orphanages = db.query(models.Orphanage).all()
    return orphanages


# Update Orphanage
@router.put("/update/{orphanage_id}", response_model=OrphanageResponse)
def update_orphanage(
    orphanage_id: int,
    request: OrphanageCreate = Body(...),
    db: Session = Depends(get_db)
):
    orphanage = db.query(models.Orphanage).filter(models.Orphanage.orphanage_id == orphanage_id).first()
    
    if not orphanage:
        return {"error": "Orphanage not found"}
    
    orphanage.name = request.name
    orphanage.address = request.address
    orphanage.city = request.city
    orphanage.contact = request.contact
    orphanage.description = request.description

    db.commit()
    db.refresh(orphanage)

    return orphanage

@router.delete("/delete/{orphanage_id}")
def delete_orphanage(orphanage_id: int, db: Session = Depends(get_db)):
    orphanage = db.query(models.Orphanage).filter(models.Orphanage.orphanage_id == orphanage_id).first()
    
    if not orphanage:
        return {"error": "Orphanage not found"}
    
    db.delete(orphanage)
    db.commit()

    return {"message": "Orphanage deleted successfully"}