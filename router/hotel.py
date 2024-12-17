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

@router.post("/")
def create_hotel(request: HotelBase, db: Session = Depends(get_db), current_user: UserBase = Depends(get_current_user)):
    return db_hotel.create_hotel(db, request, current_user)

@router.get('/{id}')
def get_hotel(id: int, db: Session = Depends(get_db), current_user: UserBase = Depends(get_current_user)):
    return {
        'data': db_hotel.get_hotel(db, id),
        'current_user': current_user
    }

@router.put('/{id}')
def update_hotel(request: HotelBase, id: int, db: Session = Depends(get_db), current_user: UserBase = Depends(get_current_user)):
    return db_hotel.update_hotel(db, id, request)

@router.get('/')
def get_all_hotels(db: Session = Depends(get_db)):
    return db_hotel.get_all_hotels(db)

@router.delete('/{id}')
def delete_hotel(id: int, db: Session = Depends(get_db), current_user: UserBase = Depends(get_current_user)):
    return db_hotel.delete_hotel(db, id)