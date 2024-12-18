from typing import Optional
from pydantic import BaseModel
from datetime import datetime
from enum import Enum

class UserBase(BaseModel):
   id: int
   username: str
   email: str
   password: str

class UserDisplay(BaseModel):
   id: int
   username: str
   email: str
   class Config():
      orm_mod = True

class HotelBase(BaseModel):
   id: int
   name: str
   location: str
   amenities: str
   manager_id: int

class HotelDisplay(BaseModel):
   id: int
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
   availability_status: bool = True

class RoomDisplay(BaseModel):
   id: int
   id: int
   hotel_id: int
   room_number: str
   price: float
   type: str

class BookingBase(BaseModel):
   id: int
   user_id: int
   room_id: int
   start_date: datetime
   end_date: datetime
   payment_id: int
   status: str

class PaymentBase(BaseModel):
   id: int
   booking_id: int
   transaction_amount: float
   date: datetime
   status: bool

class CommentsBase(BaseModel):
   id: int
   user_id: int
   hotel_id: int
   rating: float
   text: str
