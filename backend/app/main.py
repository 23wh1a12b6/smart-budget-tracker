from fastapi import FastAPI
from fastapi.security import HTTPBearer

from app.database import engine, Base
from app import models
from app.routers import auth, transaction

app = FastAPI()
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:3001"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# ✅ THIS IS REQUIRED FOR SWAGGER AUTH BUTTON
security = HTTPBearer()

Base.metadata.create_all(bind=engine)

app.include_router(auth.router)
app.include_router(transaction.router)