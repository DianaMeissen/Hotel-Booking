from fastapi import HTTPException, status
from db.hash import Hash
from sqlalchemy.orm.session import Session
from db.models import DbUser
from schemas import UserBase, UserPatch

def create_user(db: Session, request: UserBase):
    new_user = DbUser(
        id = request.id,
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

def get_user_by_username(db: Session, username: str):
    user = db.query(DbUser).filter(DbUser.username == username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"User with username {username} not found")
    return user

def update_user(db: Session, id: int, request: UserBase):
    user = db.query(DbUser).filter(DbUser.id == id)
    if not user.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"User with id {id} not found")
    user.update({
        DbUser.id: id,
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

def patch_user(db: Session, id: int, request: UserPatch):
    user = db.query(DbUser).filter(DbUser.id == id)
    if not user.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"User with id {id} not found")
    if request.username is not None:
        user.update({
            DbUser.username: request.username,
        })
    if request.email is not None:
        user.update({
            DbUser.email: request.email,
        })
    if request.password is not None:
        user.update({
            DbUser.password: Hash.bcrypt(request.password)
        })
    db.commit()

    return {
        "message": "User was updated",
        "user": user
    }