from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from db.database import get_db
from schemas import RoomBase, UserBase
from db import db_room
from db.models import DbHotel, DbRoom
from auth.oauth2 import get_current_user

router = APIRouter(
    prefix="/rooms",
    tags=["rooms"]
)

@router.post("/")
def create_room(
    request: RoomBase, 
    db: Session = Depends(get_db),
    current_user: UserBase = Depends(get_current_user)
):
    # Check if current user is the hotel manager
    hotel = db.query(DbHotel).filter(DbHotel.id == request.hotel_id).first()
    if not hotel:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Hotel with id {request.hotel_id} does not exists"
        )
    if hotel.manager_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only hotel manager can add rooms"
        )
    return db_room.create_room(db, request)

@router.get("/{room_id}")
def get_room(
    room_id: int,
    db: Session = Depends(get_db)
):
    return db_room.get_room(db, room_id)

@router.get("/hotel/{hotel_id}")
def get_hotel_rooms(
    hotel_id: int,
    db: Session = Depends(get_db)
):
    return db_room.get_hotel_rooms(db, hotel_id)

@router.put("/{room_id}")
def update_room(
    room_id: int,
    request: RoomBase,
    db: Session = Depends(get_db),
    current_user: UserBase = Depends(get_current_user)
):
    # Check if current user is the hotel manager
    hotel = db.query(DbHotel).filter(DbHotel.id == request.hotel_id).first()
    if not hotel or hotel.manager_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only hotel manager can update rooms"
        )
    return db_room.update_room(db, room_id, request)

@router.delete("/{room_id}")
def delete_room(
    room_id: int,
    db: Session = Depends(get_db),
    current_user: UserBase = Depends(get_current_user)
):
    # Get room and check if current user is the hotel manager
    room = db_room.get_room(db, room_id)
    hotel = db.query(DbHotel).filter(DbHotel.id == room.hotel_id).first()
    if not hotel or hotel.manager_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only hotel manager can delete rooms"
        )
    return db_room.delete_room(db, room_id)

@router.put("/{room_id}/availability")
def update_room_availability(
    room_id: int,
    availability: bool,
    db: Session = Depends(get_db),
    current_user: UserBase = Depends(get_current_user)
):
    # Get room and check if current user is the hotel manager
    room = db_room.get_room(db, room_id)
    hotel = db.query(DbHotel).filter(DbHotel.id == room.hotel_id).first()
    if not hotel or hotel.manager_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only hotel manager can update room availability"
        )
    return db_room.update_room_availability(db, room_id, availability) 