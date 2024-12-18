from sqlalchemy.sql.sqltypes import Integer, String, Float, Boolean, Date, Enum
from db.database import Base
from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship
import enum

class PaymentStatus(enum.Enum):
    PENDING = "PENDING"
    SUCCESS = "SUCCESS"
    CANCELLED = "CANCELLED"

class DbUser(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key = True, index = True)
    username = Column(String)
    email = Column(String)
    password = Column(String)
    comments = Column(String)
    hotels = relationship('DbHotel', back_populates='manager')

class DbHotel(Base):
    __tablename__ = "hotels"
    id = Column(Integer, primary_key = True, index = True)
    name = Column(String)
    location = Column(String)
    contact_info = Column(String)
    amenities = Column(String)
    manager_id = Column(Integer, ForeignKey("users.id"))
    manager = relationship("DbUser", back_populates='hotels')
    rating = Column(Float, ForeignKey("comments.rating"))  # Is it must be like that bcs rating must be calculated from relative comments from comments table
    comments = Column(String)

class DbRoom(Base):
    __tablename__ = "rooms"
    id = Column(Integer, primary_key = True, index = True)
    hotel_id = Column(Integer) # relationship("DbHotel", back_populates='rooms') this logic must be added to the hotel obj
    room_number = Column(String)
    price = Column(Float)
    type = Column(String)
    availability_status = Column(Boolean)

class DbBooking(Base):
    __tablename__ = "bookings"
    id = Column(Integer, primary_key = True, index = True)
    user_id = Column(Integer, ForeignKey("users.id")) # ask maybe it is better to use relationships()
    room_id = Column(Integer, ForeignKey("rooms.id"))
    start_date = Column(Date)
    end_date = Column(Date)
    payment_id = Column(Integer)

class DbPayment(Base):
    __tablename__ = "payments"
    id = Column(Integer, primary_key = True, index = True)
    booking_id = Column(Integer, ForeignKey("bookings.id"))
    transaction_amount = Column(Float)
    date = Column(Date)
    status = Column(Enum(PaymentStatus), default=PaymentStatus.PENDING)

class DbComment(Base):
    __tablename__ = "comments"
    id = Column(Integer, primary_key = True, index = True)
    user_id = Column(Integer, ForeignKey("users.id"))
    hotel_id = Column(Integer, ForeignKey("hotels.id"))
    rating = Column(Float)
    text = Column(String)