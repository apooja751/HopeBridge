from fastapi import FastAPI
from app.database import engine, Base
from app.models import models
from app.routes import auth
from app.routes import donor

app = FastAPI(title="HopeBridge API", version="1.0.0")

app.include_router(donor.router)

models.Base.metadata.create_all(bind=engine)

# Routes
app.include_router(auth.router)

@app.get("/")
def root():
    return {"message": "HopeBridge Backend is Running!"}