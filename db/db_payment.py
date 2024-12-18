from fastapi import HTTPException, status
from sqlalchemy.orm.session import Session
from db.models import DbBooking, DbPayment, DbRoom, PaymentStatus
from schemas import PaymentBase
from datetime import datetime

def create_payment(db: Session, request: PaymentBase):
    booking = db.query(DbBooking).filter(DbBooking.id == request.booking_id).first()
    if not booking:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"Booking with id {request.booking_id} not found"
        )
    
    room = db.query(DbRoom).filter(DbRoom.id == booking.room_id).first()
    if not room:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Room not found"
        )
        
    if room.price > request.transaction_amount:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Not enough money. Actual room price is {room.price}"
        )

    new_payment = DbPayment(
        booking_id=request.booking_id,
        transaction_amount=request.transaction_amount,
        date=datetime.now(),
        status=PaymentStatus.PENDING  # Default status
    )
    
    db.add(new_payment)
    db.commit()
    db.refresh(new_payment)

    return new_payment

def update_payment_status(db: Session, payment_id: int, new_status: PaymentStatus):
    payment = db.query(DbPayment).filter(DbPayment.id == payment_id).first()
    if not payment:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Payment with id {payment_id} not found"
        )
    
    payment.status = new_status
    db.commit()
    db.refresh(payment)
    return payment