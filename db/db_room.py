from fastapi import HTTPException, status
from sqlalchemy.orm.session import Session
from db.models import DbRoom, DbHotel
from schemas import RoomBase

def create_room(db: Session, request: RoomBase):
    # Check if hotel exists
    hotel = db.query(DbHotel).filter(DbHotel.id == request.hotel_id).first()
    if not hotel:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Hotel with id {request.hotel_id} not found"
        )
    
    # Check if room number already exists in the hotel
    existing_room = db.query(DbRoom).filter(
        DbRoom.hotel_id == request.hotel_id,
        DbRoom.room_number == request.room_number
    ).first()
    
    if existing_room:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Room number {request.room_number} already exists in this hotel"
        )

    new_room = DbRoom(
        hotel_id=request.hotel_id,
        room_number=request.room_number,
        price=request.price,
        type=request.type,
        availability_status=True  # Default to available
    )
    
    db.add(new_room)
    db.commit()
    db.refresh(new_room)
    return new_room

def get_room(db: Session, room_id: int):
    room = db.query(DbRoom).filter(DbRoom.id == room_id).first()
    if not room:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Room with id {room_id} not found"
        )
    return room

def get_hotel_rooms(db: Session, hotel_id: int):
    hotel = db.query(DbHotel).filter(DbHotel.id == hotel_id).first()
    if not hotel:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Hotel with id {hotel_id} not found"
        )
    
    return db.query(DbRoom).filter(DbRoom.hotel_id == hotel_id).all()

def update_room(db: Session, room_id: int, request: RoomBase):
    room = db.query(DbRoom).filter(DbRoom.id == room_id)
    if not room.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Room with id {room_id} not found"
        )
    
    # Check if the new room number already exists (if room number is being changed)
    if request.room_number != room.first().room_number:
        existing_room = db.query(DbRoom).filter(
            DbRoom.hotel_id == request.hotel_id,
            DbRoom.room_number == request.room_number
        ).first()
        
        if existing_room:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Room number {request.room_number} already exists in this hotel"
            )

    room.update({
        DbRoom.hotel_id: request.hotel_id,
        DbRoom.room_number: request.room_number,
        DbRoom.price: request.price,
        DbRoom.type: request.type,
        DbRoom.availability_status: request.availability_status
    })
    
    db.commit()
    return "Room updated successfully"

def delete_room(db: Session, room_id: int):
    room = db.query(DbRoom).filter(DbRoom.id == room_id).first()
    if not room:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Room with id {room_id} not found"
        )
    
    # Check if room has any active bookings before deletion
    # This check would need to be implemented based on your booking system
    
    db.delete(room)
    db.commit()
    return "Room deleted successfully"

def update_room_availability(db: Session, room_id: int, availability: bool):
    room = db.query(DbRoom).filter(DbRoom.id == room_id)
    if not room.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Room with id {room_id} not found"
        )
    
    room.update({
        DbRoom.availability_status: availability
    })
    
    db.commit()
    return f"Room availability updated to {'available' if availability else 'unavailable'}"
