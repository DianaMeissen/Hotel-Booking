from typing import List, Optional
from pydantic import BaseModel

# User inside Comment 
class User(BaseModel):
   id: int
   username: str
   class Config():
      orm_mod = True


class Comment(BaseModel):
   user: User
   rating: int
   comment: str
   hotel_name: str
   class Config(): # needed to convert from db object to object
      orm_mod = True

class UserBase(BaseModel):
   username: str
   email: str
   password: str
   comments: Optional[List[Comment]] = []

class UserDisplay(BaseModel):
   username: str
   email: str
   class Config():
      orm_mod = True



class HotelBase(BaseModel):
   name: str
   location: str
   contact_info: str
   amenities: str
   manager_id: int
   rating: Optional[float] 
   comments: Optional[List[Comment]] = []

class HotelDisplay(BaseModel):
   name: str
   location: str
   contact_info: str
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
   #  start_date: date
   #  end_date: date
    payment_id: int

class PaymentBase(BaseModel):
    booking_id: int
    transaction_amount: float
   #  date: date
    status: bool
