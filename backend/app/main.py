from fastapi import FastAPI
from app.database import engine, Base
from app.models import models
from app.routes import auth

app = FastAPI(title="HopeBridge API", version="1.0.0")

models.Base.metadata.create_all(bind=engine)

# Routes
app.include_router(auth.router)

@app.get("/")
def root():
    return {"message": "HopeBridge Backend is Running!"}