from fastapi import HTTPException, status
from sqlalchemy.orm.session import Session
from db.models import DbHotel, DbUser
from schemas import HotelBase, UserBase

def create_hotel(db: Session, request: HotelBase, current_user: UserBase):  
    if current_user.id != request.manager_id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, 
            detail=f"You can't create hotel with another manager")        
    
    new_hotel = DbHotel(
        id = request.id,
        name = request.name,
        location = request.location,
        amenities = request.amenities or None,
        manager_id = request.manager_id
    )
    db.add(new_hotel)
    db.commit()
    db.refresh(new_hotel)

    return new_hotel

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

def update_hotel(db: Session, id: int, request: HotelBase, current_user: UserBase):
    hotel = db.query(DbHotel).filter(DbHotel.id == id)

    if not hotel.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"Hotel with id {id} not found")

    if current_user.id is not hotel.first().manager_id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, 
            detail="Request rejected. Hotel can be updated only by it's manager")

    hotel.update({
        DbHotel.id: request.id,
        DbHotel.name: request.name,
        DbHotel.location: request.location,
        DbHotel.amenities: request.amenities or None,
        DbHotel.manager_id: request.manager_id
    })
    db.commit()

    return "Hotel was updated"

def delete_hotel(db: Session, id: int):
    hotel = db.query(DbHotel).filter(DbHotel.id == id).first()
    if not hotel.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"Hotel with id {id} not found")
    db.delete(hotel)
    db.commit()

    return "Hotel was deleted succesfully"