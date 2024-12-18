from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from auth.oauth2 import get_current_user
from db.database import get_db
from schemas import BookingBase

from db import db_booking

router = APIRouter(
    prefix="/booking",
    tags=["booking"]
)

@router.post("/")
def create_booking(request:BookingBase, db: Session = Depends(get_db), current_user: BookingBase = Depends(get_current_user)):
    return db_booking.create_booking(db, request, current_user)

# @router.put('/{id}')
# def process_payment(id: int, db: Session = Depends(get_db), current_user: BookingBase = Depends(get_current_user)):
#     return db_booking.process_payment(db, id)