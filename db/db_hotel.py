from fastapi import HTTPException, status
from sqlalchemy.orm.session import Session
from auth.oauth2 import get_current_user
from db.models import DbHotel, DbUser
from schemas import HotelBase, UserBase

def create_hotel(db: Session, request: HotelBase, current_user: UserBase):  
    if current_user.id == request.manager_id:
        new_hotel = DbHotel(
            name = request.name,
            location = request.location,
            amenities = request.amenities or None,
            manager_id = request.manager_id
        )
        db.add(new_hotel)
        db.commit()
        db.refresh(new_hotel)

        return new_hotel
    else:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, 
            detail=f"You can't create hotel with another manager")

def get_hotel(db: Session, id: int):
    hotel = db.query(DbHotel).filter(DbHotel.id == id).first()
    # contact_info = db.query(DbUser).filter(DbUser.id == DbHotel.manager_id).first()
    # hotel.contact_info = contact_info
    if not hotel:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"Hotel with id {id} not found")
    return hotel

def get_all_hotels(db: Session):
    return db.query(DbHotel).all()

def update_hotel(db: Session, id: int, request: HotelBase):
    hotel = db.query(DbHotel).filter(DbHotel.id == id)
    current_user = get_current_user()
    if not hotel.fisrt():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"Hotel with id {id} not found")
    if current_user.id == hotel.manager_id:
        hotel.update({
            DbHotel.name: request.name,
            DbHotel.location: request.location,
            DbHotel.amenities: request.amenities or None,
            DbHotel.manager_id: request.manager_id
        })
        db.commit()

        return "Hotel was updated"
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, 
            detail="Request rejected. Hotel can be updated only by it's manager")

def delete_hotel(db: Session, id: int):
    hotel = db.query(DbHotel).filter(DbHotel.id == id).first()
    if not hotel.fisrt():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"Hotel with id {id} not found")
    db.delete(hotel)
    db.commit()

    return "Hotel was deleted succesfully"