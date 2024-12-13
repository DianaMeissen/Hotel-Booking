from sqlalchemy.sql.sqltypes import Integer, String, Float, Boolean, Date
from db.database import Base
from sqlalchemy import Column

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
    contact_info = Column(String)
    amenities = Column(String)
    manager_id = Column(String)
    rating = Column(Float)  # this field is optional and appears after users leave a review

class DbRoom(Base):
    __tablename__ = "rooms"
    id = Column(Integer, primary_key = True, index = True)
    hotel_id = Column(String)
    room_number = Column(String)
    price = Column(Float)
    type = Column(String)
    availability_status = Column(Boolean)

class DbBooking(Base):
    __tablename__ = "bookings"
    id = Column(Integer, primary_key = True, index = True)
    user_id = Column(String)
    room_id = Column(String)
    start_date = Column(Date)
    end_date = Column(Date)
    payment_id = Column(String)

class DbPayment(Base):
    __tablename__ = "payments"
    id = Column(Integer, primary_key = True, index = True)
    booking_id = Column(String)
    transaction_amount = Column(Float)
    date = Column(Date)
    status = Column(Boolean)
