from fastapi import FastAPI
from router import user, hotel, payment, room, payment, booking
from db import models
from db.database import engine
from router import authentification
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.include_router(authentification.router)
app.include_router(user.router)
app.include_router(hotel.router)
app.include_router(payment.router)
app.include_router(room.router)
app.include_router(booking.router)

@app.get('/')
def index():
    return {"message": "Welcome to the booking service"}

models.Base.metadata.create_all(engine)

origins = ['http://localhost:3000']

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins, 
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"]
)