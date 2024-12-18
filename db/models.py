from sqlalchemy.sql.sqltypes import Integer, String, Float, Boolean, Date, Enum
from db.database import Base
from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship
import enum

class DbUser(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key = True, index = True)
    username = Column(String)
    email = Column(String)
    password = Column(String)

class DbHotel(Base):
    __tablename__ = "hotels"
    id = Column(Integer, primary_key = True, index = True)
    name = Column(String)
    location = Column(String)
    amenities = Column(String)
    manager_id = Column(Integer, ForeignKey("users.id"))

class DbRoom(Base):
    __tablename__ = "rooms"
    id = Column(Integer, primary_key = True, index = True)
    hotel_id = Column(Integer, ForeignKey("hotels.id"))
    room_number = Column(String)
    price = Column(Float)
    type = Column(String)
    availability_status = Column(Boolean)

class DbBooking(Base):
    __tablename__ = "bookings"
    id = Column(Integer, primary_key = True, index = True)
    user_id = Column(Integer, ForeignKey("users.id"))
    room_id = Column(Integer, ForeignKey("rooms.id"))
    start_date = Column(Date)
    end_date = Column(Date)
    payment_id = Column(Integer, ForeignKey("payments.id"))
    status = Column(String)

class DbPayment(Base):
    __tablename__ = "payments"
    id = Column(Integer, primary_key = True, index = True)
    booking_id = Column(Integer, ForeignKey("bookings.id"))
    transaction_amount = Column(Float)
    date = Column(Date)
    status = Column(Boolean)

class DbComment(Base):
    __tablename__ = "comments"
    id = Column(Integer, primary_key = True, index = True)
    user_id = Column(Integer, ForeignKey("users.id"))
    hotel_id = Column(Integer, ForeignKey("hotels.id"))
    rating = Column(Float)
    text = Column(String)