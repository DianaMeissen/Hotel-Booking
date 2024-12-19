from fastapi import HTTPException, status
from sqlalchemy.orm.session import Session
from db.models import DbBooking, DbHotel, DbRoom, DbUser
from schemas import BookingBase, UserBase

def create_booking(db: Session, request: BookingBase, current_user: UserBase):  
    if current_user.id != request.user_id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, 
            detail=f"You can't create booking for another user")          
    
    room = db.query(DbRoom).filter(DbRoom.id == request.room_id).first()
    if not room:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"Room with id {request.room_id} doen't exists")    

    hotel = db.query(DbHotel).filter(DbHotel.id == room.hotel_id).first()
    if current_user.id == hotel.manager_id:
        print(current_user.id, hotel.manager_id)
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, 
            detail=f"You can't create booking in your own hotel")  
    # check room availability
    
    new_booking = DbBooking(
        # id = request.id,
        user_id = request.user_id,
        room_id = request.room_id,
        start_date = request.start_date,
        end_date = request.end_date,
        # payment_id = request.payment_id,
        status = request.status
    )
    db.add(new_booking)
    db.commit()
    db.refresh(new_booking)

    return new_booking