from pydantic import BaseModel
from datetime import datetime

class UserBase(BaseModel):
   username: str
   email: str
   password: str

class UserDisplay(BaseModel):
   username: str
   email: str
   class Config():
      orm_mod = True

class HotelBase(BaseModel):
   name: str
   location: str
   amenities: str
   manager_id: int

class HotelDisplay(BaseModel):
   name: str
   location: str
   amenities: str
   class Config():
      orm_mod = True

class RoomBase(BaseModel):
   hotel_id: int
   room_number: str
   price: float
   type: str

class BookingBase(BaseModel):
   user_id: int
   room_id: int
   start_date: datetime
   end_date: datetime
   payment_id: int
   status: str

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
