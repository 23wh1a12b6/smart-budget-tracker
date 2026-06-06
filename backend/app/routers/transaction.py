from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel

from app.database import SessionLocal
from app import models
from app.models import TransactionType
from app.deps import get_current_user
from app.database import SessionLocal
from fastapi import Depends, HTTPException


router = APIRouter()
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class TransactionSchema(BaseModel):
    type: TransactionType
    amount: float
    category: str
    description: str


@router.post("/transactions")
def create_transaction(
    data: TransactionSchema,   # 🔥 FIX HERE (BODY)
    db: Session = Depends(get_db),
    user_id: int = Depends(get_current_user)
):

    new_txn = models.Transaction(
        user_id=user_id,
        type=data.type,
        amount=data.amount,
        category=data.category,
        description=data.description
    )

    db.add(new_txn)
    db.commit()
    db.refresh(new_txn)

    return {"message": "Transaction added"}
@router.get("/transactions")
def get_transactions(
    db: Session = Depends(get_db),
    user_id: int = Depends(get_current_user)
):
    txns = db.query(models.Transaction).filter(models.Transaction.user_id == user_id).all()
    return txns
@router.delete("/transactions/{id}")
def delete_transaction(
    id: int,
    db: Session = Depends(get_db),
    user_id: int = Depends(get_current_user)
):
    txn = db.query(models.Transaction).filter(
        models.Transaction.id == id,
        models.Transaction.user_id == user_id
    ).first()

    if not txn:
        raise HTTPException(status_code=404, detail="Transaction not found")

    db.delete(txn)
    db.commit()

    return {"message": "Deleted successfully"}
from app.schemas import TransactionUpdate  # ADD THIS IMPORT

@router.put("/transactions/{id}")
def update_transaction(
    id: int,
    data: TransactionUpdate,   # 👈 CHANGE THIS
    db: Session = Depends(get_db),
    user_id: int = Depends(get_current_user)
):
    txn = db.query(models.Transaction).filter(
        models.Transaction.id == id,
        models.Transaction.user_id == user_id
    ).first()

    if not txn:
        raise HTTPException(status_code=404, detail="Transaction not found")

    txn.type = data.type
    txn.amount = data.amount
    txn.category = data.category
    txn.description = data.description

    db.commit()
    db.refresh(txn)

    return {"message": "Updated successfully"}