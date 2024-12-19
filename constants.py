from enum import Enum

class Booking_status(Enum):
    SUCCESS = "SUCCESS" 
    PENDING = "PENDING"
    CANCELED = "CANCELED"

class Amenities(Enum):
    POOL = "POOL"
    WIFI = "WIFI"
    BREAKFAST = "BREAKFAST"
    TV = "TV"
    SAUNA = "SAUNA"
    FITNESS = "FITNESS"

class Room_type(Enum):
    STANDART = "STANDART"
    SINGLE = "SINGLE"
    DOUBLE = "DOUBLE"
    SUITE = "SUITE"
    FAMILY = "FAMILY"
    SUPERIOR = "SUPERIOR"
    DELUXE = "DELUXE"

class Locations(Enum):
    CITY_CENTER = "CITY_CENTER"
    SUBURBAN = "SUBURBAN"
    AIRPORT = "AIRPORT"
    MOUNTAIN = "MOUNTAIN"
    SEA_FRONT = "SEA_FRONT"