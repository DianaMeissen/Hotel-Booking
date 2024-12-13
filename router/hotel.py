from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.database import get_db
from schemas import HotelBase

from db import db_hotel

router = APIRouter(
    prefix="/user/{user_id}/hotel",
    tags=["hotel"]
)

# Crearte hotel
@router.post("/")
def create_user(request:HotelBase, db: Session = Depends(get_db)):
    return db_hotel.create_hotel(db, request)