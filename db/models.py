from sqlalchemy.sql.sqltypes import Integer, String, Float
from db.database import Base
from sqlalchemy import Column

class DbUser(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key = True, index = True)
    username = Column(String)
    email = Column(String)
    password = Column(String)

class DbHotel(Base):
    __tablename__ = "hotels"
    id = Column(Integer, primary_key = True, index = True)
    name = Column(String)
    location = Column(String)
    contact_info = Column(String)
    amenities = Column(String)
    manager_id = Column(String)