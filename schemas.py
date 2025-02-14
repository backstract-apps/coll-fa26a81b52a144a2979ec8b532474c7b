from pydantic import BaseModel

import datetime

import uuid

from typing import Any, Dict, List, Tuple

class Users(BaseModel):
    id: int
    created_at: datetime.date
    name: str
    email: str
    password: str


class ReadUsers(BaseModel):
    id: int
    created_at: datetime.date
    name: str
    email: str
    password: str
    class Config:
        from_attributes = True


class ParkingLots(BaseModel):
    id: int
    created_at: datetime.date
    name: str
    location: str
    capacity: int
    user_id: int


class ReadParkingLots(BaseModel):
    id: int
    created_at: datetime.date
    name: str
    location: str
    capacity: int
    user_id: int
    class Config:
        from_attributes = True


class ParkingSlots(BaseModel):
    id: int
    created_at: datetime.date
    type: str
    is_occupied: str
    price_per_hour: int
    parking_lot_id: int


class ReadParkingSlots(BaseModel):
    id: int
    created_at: datetime.date
    type: str
    is_occupied: str
    price_per_hour: int
    parking_lot_id: int
    class Config:
        from_attributes = True


class Vehicle(BaseModel):
    id: int
    created_at: datetime.date
    registration_id: int
    owner_name: str
    phone_number: int
    model_type: str
    color: str
    parking_lot_id: int
    parking_slot_id: int


class ReadVehicle(BaseModel):
    id: int
    created_at: datetime.date
    registration_id: int
    owner_name: str
    phone_number: int
    model_type: str
    color: str
    parking_lot_id: int
    parking_slot_id: int
    class Config:
        from_attributes = True


class ParkingHistory(BaseModel):
    id: int
    created_at: datetime.date
    vehicle_id: int
    parking_slot_id: int
    clock_in: datetime.date
    clock_out: datetime.date
    total_amount: int


class ReadParkingHistory(BaseModel):
    id: int
    created_at: datetime.date
    vehicle_id: int
    parking_slot_id: int
    clock_in: datetime.date
    clock_out: datetime.date
    total_amount: int
    class Config:
        from_attributes = True




class PostUsers(BaseModel):
    id: str
    created_at: str
    name: str
    email: str
    password: str

    class Config:
        from_attributes = True



class PutUsersId(BaseModel):
    id: str
    created_at: str
    name: str
    email: str
    password: str

    class Config:
        from_attributes = True



class PostParkingLots(BaseModel):
    id: str
    created_at: str
    name: str
    location: str
    capacity: str
    user_id: str

    class Config:
        from_attributes = True



class PutParkingLotsId(BaseModel):
    id: str
    created_at: str
    name: str
    location: str
    capacity: str
    user_id: str

    class Config:
        from_attributes = True



class PostParkingSlots(BaseModel):
    id: str
    created_at: str
    type: str
    is_occupied: str
    price_per_hour: str
    parking_lot_id: str

    class Config:
        from_attributes = True



class PutParkingSlotsId(BaseModel):
    id: str
    created_at: str
    type: str
    is_occupied: str
    price_per_hour: str
    parking_lot_id: str

    class Config:
        from_attributes = True



class PostVehicle(BaseModel):
    id: str
    created_at: str
    registration_id: int
    owner_name: str
    phone_number: int
    model_type: str
    color: str
    parking_lot_id: str
    parking_slot_id: str

    class Config:
        from_attributes = True



class PutVehicleId(BaseModel):
    id: str
    created_at: str
    registration_id: str
    owner_name: str
    phone_number: str
    model_type: str
    color: str
    parking_lot_id: str
    parking_slot_id: str

    class Config:
        from_attributes = True



class PostParkingHistory(BaseModel):
    id: str
    created_at: str
    vehicle_id: int
    parking_slot_id: int
    clock_in: str
    clock_out: str
    total_amount: int

    class Config:
        from_attributes = True



class PutParkingHistoryId(BaseModel):
    id: str
    created_at: str
    vehicle_id: str
    parking_slot_id: str
    clock_in: str
    clock_out: str
    total_amount: str

    class Config:
        from_attributes = True



class PostLogin(BaseModel):
    email: str
    password: str

    class Config:
        from_attributes = True



class PostSignup(BaseModel):
    name: str
    email: str
    password: str

    class Config:
        from_attributes = True

