from fastapi import HTTPException, status
from db.hash import Hash
from sqlalchemy.orm.session import Session
from db.models import DbBooking, DbPayment, DbRoom
from schemas import UserBase
from datetime import datetime

def create_payment(db: Session, request: UserBase):
    booking = db.query(DbBooking).filter(DbBooking.id == request.booking_id).first()
    room_price = db.query(DbRoom).filter(DbRoom.id == booking.room_id).first()
    if not booking:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"Booking with id {id} not found")
    if room_price < request.transaction_amount:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, 
            detail=f"Not enough money. Actual room price is {room_price}")
    new_payment = DbPayment(
        booking_id = request.booking_id,
        transaction_amount = request.transaction_amount,
        date = datetime.utcnow() # Google what method is not deprecated
        # status = Column(Boolean) #SHould we create in db payment with status rejected, or should we add logic where payment will be pending and the proccesed
    )
    db.add(new_payment)
    db.commit()
    db.refresh(new_payment)

    return new_payment