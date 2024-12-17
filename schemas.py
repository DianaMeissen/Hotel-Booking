from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime

# User inside Comment 
class User(BaseModel):
   id: int
   username: str
   class Config():
      orm_mod = True

class ContactInfo(BaseModel):
   username: str
   email: str
   class Config():
      orm_mod = True

class Hotel(BaseModel):
   id: int
   name: str
   class Config():
      orm_mod = True


class Comment(BaseModel):
   user: User
   rating: float
   comment: str
   hotel_id: int
   class Config(): # needed to convert from db object to object
      orm_mod = True

class UserBase(BaseModel):
   username: str
   email: str
   password: str
   comments: Optional[List[Comment]] = []
   hotels: Optional[List[Hotel]] = []

class UserDisplay(BaseModel):
   username: str
   email: str
   hotels: Optional[List[Hotel]] = []
   class Config():
      orm_mod = True



class HotelBase(BaseModel):
   name: str
   location: str
   contact_info: ContactInfo
   amenities: str
   manager_id: int
   rating: Optional[float] 
   comments: Optional[List[Comment]] = []

class HotelDisplay(BaseModel):
   name: str
   location: str
   contact_info: ContactInfo
   amenities: str
   manager: User
   rating: Optional[float] 
   class Config():
      orm_mod = True


class RoomBase(BaseModel):
   hotel_id: int
   room_number: str
   price: float
   type: str
   availability_status: bool

class BookingBase(BaseModel):
    user_id: int
    room_id: int
   #  start_date: datetime.utcnow()    ----> ask is it working
    start_date: datetime
    end_date: datetime
    payment_id: int

class PaymentBase(BaseModel):
    booking_id: int
    transaction_amount: float
    date: datetime
    status: bool

class CommentsBase(BaseModel):
   user_id: int
   hotel_id: int
   rating: float
   text: str
