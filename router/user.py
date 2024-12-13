from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.database import get_db
from schemas import UserBase, UserDisplay

from db import db_user

router = APIRouter(
    prefix="/user",
    tags=["user"]
)

# Crearte user
@router.post("/", response_model=UserDisplay)
def create_user(request:UserBase, db: Session = Depends(get_db)):
    return db_user.create_user(db, request)

# Read all users

# Read one user

# Update user

# Delete user