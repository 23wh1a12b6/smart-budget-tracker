from pydantic import BaseModel
from typing import Optional
from app.models import TransactionType

class UserCreate(BaseModel):
    name: str
    email: str
    password: str

class UserLogin(BaseModel):
    email: str
    password: str
class TransactionUpdate(BaseModel):
    type: str
    amount: float
    category: str
    description: str
# class TransactionCreate(BaseModel):
#     type: TransactionType
#     amount: float
#     category: Optional[str] = "general"
#     description: Optional[str] = None