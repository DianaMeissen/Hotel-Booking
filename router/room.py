from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from db.database import get_db
from schemas import RoomBase, RoomDisplay, UserBase
from db import db_room, db_hotel
from auth.oauth2 import get_current_user

router = APIRouter(
    prefix="/room",
    tags=["room"]
)

@router.post("/", response_model=RoomDisplay)
def create_room(
    request: RoomBase, 
    db: Session = Depends(get_db),
    current_user: UserBase = Depends(get_current_user)
):
    # Check if current user is the hotel manager
    hotel = db.query(db_hotel.DbHotel).filter(db_hotel.DbHotel.id == request.hotel_id).first()
    if not hotel or hotel.manager_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only hotel manager can add rooms"
        )
    return db_room.create_room(db, request)

@router.get("/{room_id}", response_model=RoomDisplay)
def get_room(
    room_id: int,
    db: Session = Depends(get_db)
):
    return db_room.get_room(db, room_id)

@router.get("/hotel/{hotel_id}", response_model=List[RoomDisplay])
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
    hotel = db.query(db_hotel.DbHotel).filter(db_hotel.DbHotel.id == request.hotel_id).first()
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
    hotel = db.query(db_hotel.DbHotel).filter(db_hotel.DbHotel.id == room.hotel_id).first()
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
    hotel = db.query(db_hotel.DbHotel).filter(db_hotel.DbHotel.id == room.hotel_id).first()
    if not hotel or hotel.manager_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only hotel manager can update room availability"
        )
    return db_room.update_room_availability(db, room_id, availability) 