from sqlalchemy.orm.session import Session
from db.models import DbHotel
from schemas import HotelBase

def create_hotel(db: Session, request: HotelBase):
    new_hotel = DbHotel(
        name = request.name,
        location = request.location,
        contact_info = request.contact_info,
        amenities = request.amenities or None,
        manager_id = request.user_id
    )
    db.add(new_hotel)
    db.commit()
    db.refresh(new_hotel)

    return new_hotel

def get_all_hotels(db: Session):
    return db.query(DbHotel).all()