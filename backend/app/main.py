from app.routes import request
from fastapi import FastAPI
from app.routes import orphanage
from app.database import engine, Base
from app.models import models
from app.routes import auth

app = FastAPI(title="HopeBridge API", version="1.0.0")

models.Base.metadata.create_all(bind=engine)

# Routes
app.include_router(auth.router)
app.include_router(orphanage.router)
app.include_router(request.router)

@app.get("/")
def root():
    return {"message": "HopeBridge Backend is Running!"}