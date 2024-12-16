from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.database import get_db
from schemas import UserBase, HotelBase
from auth.oauth2 import get_current_user, oauth2_scheme

from db import db_hotel

router = APIRouter(
    prefix="/hotel",
    tags=["hotel"]
)

# Crearte hotel
@router.post("/")
def create_hotel(request: HotelBase, db: Session = Depends(get_db)):
    return db_hotel.create_hotel(db, request)

@router.get('/{id}')
def get_hotel(id: int, db: Session = Depends(get_db), current_user: UserBase = Depends(get_current_user)):
    return {
        'data': db_hotel.get_hotel(db, id),
        'current_user': current_user
    }