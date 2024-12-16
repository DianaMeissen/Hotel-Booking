from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.database import get_db
from schemas import HotelBase, HotelDisplay
from auth.oauth2 import oauth2_scheme

from db import db_hotel

router = APIRouter(
    prefix="/hotel",
    tags=["hotel"]
)

# Crearte hotel
@router.post("/")
def create_hotel(request: HotelBase, db: Session = Depends(get_db)):
    return db_hotel.create_hotel(db, request)

@router.get('/{id}', response_model=HotelDisplay)
def get_hotel(id: int, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    return db_hotel.get_hotel(db, id)