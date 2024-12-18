from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from auth.oauth2 import get_current_user
from db.database import get_db
from schemas import PaymentBase

from db import db_payment

router = APIRouter(
    prefix="/payment",
    tags=["payment"]
)

@router.post("/")
def create_payment(request:PaymentBase, db: Session = Depends(get_db), current_user: PaymentBase = Depends(get_current_user)):
    return db_payment.create_payment(db, request)

@router.put('/{id}')
def process_payment(id: int, db: Session = Depends(get_db), current_user: PaymentBase = Depends(get_current_user)):
    return db_payment.process_payment(db, id)