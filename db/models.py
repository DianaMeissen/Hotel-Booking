from sqlalchemy.sql.sqltypes import Integer, String, Float, Boolean, Date
from db.database import Base
from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship

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
    rating = Column(Float)  # this field is optional and appears after users leave a review
    comments = Column(String)

class DbRoom(Base):
    __tablename__ = "rooms"
    id = Column(Integer, primary_key = True, index = True)
    hotel_id = Column(Integer)
    room_number = Column(String)
    price = Column(Float)
    type = Column(String)
    availability_status = Column(Boolean)

class DbBooking(Base):
    __tablename__ = "bookings"
    id = Column(Integer, primary_key = True, index = True)
    user_id = Column(Integer)
    room_id = Column(Integer)
    start_date = Column(Date)
    end_date = Column(Date)
    payment_id = Column(Integer)

class DbPayment(Base):
    __tablename__ = "payments"
    id = Column(Integer, primary_key = True, index = True)
    booking_id = Column(Integer)
    transaction_amount = Column(Float)
    date = Column(Date)
    status = Column(Boolean)
