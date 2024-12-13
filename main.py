from fastapi import FastAPI
from router import user, hotel
from db import models
from db.database import engine

app = FastAPI()
app.include_router(user.router)
app.include_router(hotel.router)

@app.get('/')
def index():
    return {"message": "Welcome to the booking service"}

models.Base.metadata.create_all(engine)