from pydantic import BaseModel

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
   contact_info: str
   amenities: str
   manager_id: str
   rating: float  # this field is optional and appears after users leave a review


class RoomBase(BaseModel):
   hotel_id: str
   room_number: str
   price: float
   type: str
   availability_status: bool

class BookingBase(BaseModel):
    user_id: str
    room_id: str
   #  start_date: date
   #  end_date: date
    payment_id: str

class PaymentBase(BaseModel):
    booking_id: str
    transaction_amount: float
   #  date: date
    status: bool
