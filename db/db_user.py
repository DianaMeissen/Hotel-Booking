from fastapi import HTTPException, status
from auth import oauth2
from db.hash import Hash
from sqlalchemy.orm.session import Session
from db.models import DbUser
from schemas import UserBase

def create_user(db: Session, request: UserBase):
    new_user = DbUser(
        # id = request.id,
        username = request.username,
        email = request.email,
        password = Hash.bcrypt(request.password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return new_user

def get_all_users(db: Session): # TODO: allow this functionality to admin role
    return db.query(DbUser).all()

def get_user(db: Session, id: int):
    user = db.query(DbUser).filter(DbUser.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"User with id {id} not found")
    return user

def get_user_by_id(db: Session, id: int):
    user = db.query(DbUser).filter(DbUser.id == id).first()
    if not user:
        return None
    return user

# TODO fix this method
def update_user(db: Session, id: int, request: UserBase):
    user = db.query(DbUser).filter(DbUser.id == id)
    if not user.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"User with id {id} not found")
    
    user.update({
        # DbUser.id: id,
        DbUser.username: request.username,
        DbUser.email: request.email,
        DbUser.password: Hash.bcrypt(request.password) # this must be mooved to 'forget password' functionality
    })
    db.commit()

    return {
        "message": "User was updated",
        "user": user
    }

def delete_user(db: Session, id: int):
    user = db.query(DbUser).filter(DbUser.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"User with id {id} not found")
    db.delete(user)
    db.commit()

    return "User was deleted succesfully"
