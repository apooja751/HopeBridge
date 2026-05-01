from fastapi import FastAPI
from app.database import engine
from app.models import models

# ✅ Import routers (clean way)
from app.routes import (
    auth,
    orphanage,
    request,
    donor,
    donation,
    notification,
    message,
    inquiry,
    admin,
    status
)

app = FastAPI(title="HopeBridge API", version="1.0.0")

# ✅ Create tables
models.Base.metadata.create_all(bind=engine)

# ✅ Include routers
app.include_router(auth.router)
app.include_router(orphanage.router)
app.include_router(request.router)
app.include_router(donor.router)
app.include_router(donation.router)
app.include_router(notification.router)
app.include_router(message.router)
app.include_router(inquiry.router)
app.include_router(admin.router)
app.include_router(status.router)


@app.get("/")
def root():
    return {"message": "HopeBridge Backend is Running!"}