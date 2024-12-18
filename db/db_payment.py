from fastapi import HTTPException, status
from db.hash import Hash
from sqlalchemy.orm.session import Session
from db.models import DbBooking, DbPayment, DbRoom
from schemas import PaymentBase
from datetime import datetime

def create_payment(db: Session, request: PaymentBase):
    booking = db.query(DbBooking).filter(DbBooking.id == request.booking_id).first()
    
    if not booking:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"Booking with id {request.booking_id} not found")
    
    room = db.query(DbRoom).filter(DbRoom.id == booking.room_id).first()
    room_price = room.price

    if room_price < request.transaction_amount:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, 
            detail=f"Not enough money. Actual room price is {room_price}")
    
    new_payment = DbPayment(
        booking_id = request.booking_id,
        transaction_amount = request.transaction_amount,
        date = datetime.now(),
        status = False
    )

    db.add(new_payment)
    db.commit()
    db.refresh(new_payment)

    return new_payment

def process_payment(db: Session, id: int, request: PaymentBase):
    payment = db.query(DbPayment).filter(DbPayment.id == id)
    if not payment.fisrt():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"Payment with id {id} not found")
    payment.update({
        DbPayment.booking_id: request.booking_id,
        DbPayment.transaction_amount: request.transaction_amount,
        DbPayment.date: datetime.now(),
        DbPayment.status: True
    })
    db.commit()

    return "Payment was updated"