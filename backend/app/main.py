from fastapi import FastAPI
from app.database import engine
from app.models import models

import app.routes.inquiry as inquiry
import app.routes.message as message
import app.routes.auth as auth
import app.routes.orphanage as orphanage
import app.routes.request as request
import app.routes.donor as donor
import app.routes.donation as donation
import app.routes.notification as notification
from app.routes import admin
from app.routes import message
from app.routes import inquiry
from app.routes import notification

app = FastAPI(title="HopeBridge API", version="1.0.0")

# Create tables
models.Base.metadata.create_all(bind=engine)

# Routes
app.include_router(auth.router)
app.include_router(orphanage.router)
app.include_router(request.router)
app.include_router(donor.router)
app.include_router(donation.router)
app.include_router(notification.router)
app.include_router(message.router)
app.include_router(inquiry.router)
app.include_router(admin.router)

@app.get("/")
def root():
    return {"message": "HopeBridge Backend is Running!"}