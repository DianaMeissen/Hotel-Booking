from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.database import get_db
from schemas import PaymentBase, UserBase
from db import db_payment
from db.models import PaymentStatus
from auth.oauth2 import get_current_user

router = APIRouter(
    prefix="/payment",
    tags=["payment"]
)

@router.post("/")
def create_payment(
    request: PaymentBase, 
    db: Session = Depends(get_db),
    current_user: UserBase = Depends(get_current_user)
):
    return db_payment.create_payment(db, request)

@router.put("/{payment_id}/status/{status}")
def update_payment_status(
    payment_id: int,
    status: PaymentStatus,
    db: Session = Depends(get_db),
    current_user: UserBase = Depends(get_current_user)
):
    return db_payment.update_payment_status(db, payment_id, status) 