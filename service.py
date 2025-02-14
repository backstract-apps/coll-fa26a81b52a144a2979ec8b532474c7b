from sqlalchemy.orm import Session
from sqlalchemy import and_, or_
from typing import *
from fastapi import Request, UploadFile, HTTPException
import models, schemas
import boto3

import jwt

import datetime

from pathlib import Path

async def get_users(db: Session):

    users_all = db.query(models.Users).all()
    users_all = [new_data.to_dict() for new_data in users_all] if users_all else users_all

    res = {
        'users_all': users_all,
    }
    return res

async def get_users_id(db: Session, id: int):

    users_one = db.query(models.Users).filter(models.Users.id == id).first() 
    users_one = users_one.to_dict() if users_one else users_one

    res = {
        'users_one': users_one,
    }
    return res

async def post_users(db: Session, raw_data: schemas.PostUsers):
    id:str = raw_data.id
    created_at:str = raw_data.created_at
    name:str = raw_data.name
    email:str = raw_data.email
    password:str = raw_data.password


    record_to_be_added = {'id': id, 'created_at': created_at, 'name': name, 'email': email, 'password': password}
    new_users = models.Users(**record_to_be_added)
    db.add(new_users)
    db.commit()
    db.refresh(new_users)
    users_inserted_record = new_users.to_dict()

    res = {
        'users_inserted_record': users_inserted_record,
    }
    return res

async def put_users_id(db: Session, raw_data: schemas.PutUsersId):
    id:str = raw_data.id
    created_at:str = raw_data.created_at
    name:str = raw_data.name
    email:str = raw_data.email
    password:str = raw_data.password


    users_edited_record = db.query(models.Users).filter(models.Users.id == id).first()
    for key, value in {'id': id, 'created_at': created_at, 'name': name, 'email': email, 'password': password}.items():
          setattr(users_edited_record, key, value)
    db.commit()
    db.refresh(users_edited_record)
    users_edited_record = users_edited_record.to_dict() 

    res = {
        'users_edited_record': users_edited_record,
    }
    return res

async def delete_users_id(db: Session, id: int):

    users_deleted = None
    record_to_delete = db.query(models.Users).filter(models.Users.id == id).first()

    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        users_deleted = record_to_delete.to_dict() 

    res = {
        'users_deleted': users_deleted,
    }
    return res

async def get_parking_lots(db: Session):

    parking_lots_all = db.query(models.ParkingLots).all()
    parking_lots_all = [new_data.to_dict() for new_data in parking_lots_all] if parking_lots_all else parking_lots_all

    res = {
        'parking_lots_all': parking_lots_all,
    }
    return res

async def get_parking_lots_id(db: Session, id: int):

    parking_lots_one = db.query(models.ParkingLots).filter(models.ParkingLots.id == id).first() 
    parking_lots_one = parking_lots_one.to_dict() if parking_lots_one else parking_lots_one

    res = {
        'parking_lots_one': parking_lots_one,
    }
    return res

async def post_parking_lots(db: Session, raw_data: schemas.PostParkingLots):
    id:str = raw_data.id
    created_at:str = raw_data.created_at
    name:str = raw_data.name
    location:str = raw_data.location
    capacity:str = raw_data.capacity
    user_id:str = raw_data.user_id


    record_to_be_added = {'id': id, 'created_at': created_at, 'name': name, 'location': location, 'capacity': capacity, 'user_id': user_id}
    new_parking_lots = models.ParkingLots(**record_to_be_added)
    db.add(new_parking_lots)
    db.commit()
    db.refresh(new_parking_lots)
    parking_lots_inserted_record = new_parking_lots.to_dict()

    res = {
        'parking_lots_inserted_record': parking_lots_inserted_record,
    }
    return res

async def put_parking_lots_id(db: Session, raw_data: schemas.PutParkingLotsId):
    id:str = raw_data.id
    created_at:str = raw_data.created_at
    name:str = raw_data.name
    location:str = raw_data.location
    capacity:str = raw_data.capacity
    user_id:str = raw_data.user_id


    parking_lots_edited_record = db.query(models.ParkingLots).filter(models.ParkingLots.id == id).first()
    for key, value in {'id': id, 'created_at': created_at, 'name': name, 'location': location, 'capacity': capacity, 'user_id': user_id}.items():
          setattr(parking_lots_edited_record, key, value)
    db.commit()
    db.refresh(parking_lots_edited_record)
    parking_lots_edited_record = parking_lots_edited_record.to_dict() 

    res = {
        'parking_lots_edited_record': parking_lots_edited_record,
    }
    return res

async def delete_parking_lots_id(db: Session, id: int):

    parking_lots_deleted = None
    record_to_delete = db.query(models.ParkingLots).filter(models.ParkingLots.id == id).first()

    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        parking_lots_deleted = record_to_delete.to_dict() 

    res = {
        'parking_lots_deleted': parking_lots_deleted,
    }
    return res

async def get_parking_slots(db: Session):

    parking_slots_all = db.query(models.ParkingSlots).all()
    parking_slots_all = [new_data.to_dict() for new_data in parking_slots_all] if parking_slots_all else parking_slots_all

    res = {
        'parking_slots_all': parking_slots_all,
    }
    return res

async def get_parking_slots_id(db: Session, id: int):

    parking_slots_one = db.query(models.ParkingSlots).filter(models.ParkingSlots.id == id).first() 
    parking_slots_one = parking_slots_one.to_dict() if parking_slots_one else parking_slots_one

    res = {
        'parking_slots_one': parking_slots_one,
    }
    return res

async def post_parking_slots(db: Session, raw_data: schemas.PostParkingSlots):
    id:str = raw_data.id
    created_at:str = raw_data.created_at
    type:str = raw_data.type
    is_occupied:str = raw_data.is_occupied
    price_per_hour:str = raw_data.price_per_hour
    parking_lot_id:str = raw_data.parking_lot_id


    record_to_be_added = {'id': id, 'created_at': created_at, 'type': type, 'is_occupied': is_occupied, 'price_per_hour': price_per_hour, 'parking_lot_id': parking_lot_id}
    new_parking_slots = models.ParkingSlots(**record_to_be_added)
    db.add(new_parking_slots)
    db.commit()
    db.refresh(new_parking_slots)
    parking_slots_inserted_record = new_parking_slots.to_dict()

    res = {
        'parking_slots_inserted_record': parking_slots_inserted_record,
    }
    return res

async def put_parking_slots_id(db: Session, raw_data: schemas.PutParkingSlotsId):
    id:str = raw_data.id
    created_at:str = raw_data.created_at
    type:str = raw_data.type
    is_occupied:str = raw_data.is_occupied
    price_per_hour:str = raw_data.price_per_hour
    parking_lot_id:str = raw_data.parking_lot_id


    parking_slots_edited_record = db.query(models.ParkingSlots).filter(models.ParkingSlots.id == id).first()
    for key, value in {'id': id, 'created_at': created_at, 'type': type, 'is_occupied': is_occupied, 'price_per_hour': price_per_hour, 'parking_lot_id': parking_lot_id}.items():
          setattr(parking_slots_edited_record, key, value)
    db.commit()
    db.refresh(parking_slots_edited_record)
    parking_slots_edited_record = parking_slots_edited_record.to_dict() 

    res = {
        'parking_slots_edited_record': parking_slots_edited_record,
    }
    return res

async def delete_parking_slots_id(db: Session, id: int):

    parking_slots_deleted = None
    record_to_delete = db.query(models.ParkingSlots).filter(models.ParkingSlots.id == id).first()

    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        parking_slots_deleted = record_to_delete.to_dict() 

    res = {
        'parking_slots_deleted': parking_slots_deleted,
    }
    return res

async def get_vehicle(db: Session):

    vehicle_all = db.query(models.Vehicle).all()
    vehicle_all = [new_data.to_dict() for new_data in vehicle_all] if vehicle_all else vehicle_all

    res = {
        'vehicle_all': vehicle_all,
    }
    return res

async def get_vehicle_id(db: Session, id: int):

    vehicle_one = db.query(models.Vehicle).filter(models.Vehicle.id == id).first() 
    vehicle_one = vehicle_one.to_dict() if vehicle_one else vehicle_one

    res = {
        'vehicle_one': vehicle_one,
    }
    return res

async def post_vehicle(db: Session, raw_data: schemas.PostVehicle):
    id:str = raw_data.id
    created_at:str = raw_data.created_at
    registration_id:int = raw_data.registration_id
    owner_name:str = raw_data.owner_name
    phone_number:int = raw_data.phone_number
    model_type:str = raw_data.model_type
    color:str = raw_data.color
    parking_lot_id:str = raw_data.parking_lot_id
    parking_slot_id:str = raw_data.parking_slot_id


    record_to_be_added = {'id': id, 'created_at': created_at, 'registration_id': registration_id, 'owner_name': owner_name, 'phone_number': phone_number, 'model_type': model_type, 'color': color, 'parking_lot_id': parking_lot_id, 'parking_slot_id': parking_slot_id}
    new_vehicle = models.Vehicle(**record_to_be_added)
    db.add(new_vehicle)
    db.commit()
    db.refresh(new_vehicle)
    vehicle_inserted_record = new_vehicle.to_dict()

    res = {
        'vehicle_inserted_record': vehicle_inserted_record,
    }
    return res

async def put_vehicle_id(db: Session, raw_data: schemas.PutVehicleId):
    id:str = raw_data.id
    created_at:str = raw_data.created_at
    registration_id:str = raw_data.registration_id
    owner_name:str = raw_data.owner_name
    phone_number:str = raw_data.phone_number
    model_type:str = raw_data.model_type
    color:str = raw_data.color
    parking_lot_id:str = raw_data.parking_lot_id
    parking_slot_id:str = raw_data.parking_slot_id


    vehicle_edited_record = db.query(models.Vehicle).filter(models.Vehicle.id == id).first()
    for key, value in {'id': id, 'created_at': created_at, 'registration_id': registration_id, 'owner_name': owner_name, 'phone_number': phone_number, 'model_type': model_type, 'color': color, 'parking_lot_id': parking_lot_id, 'parking_slot_id': parking_slot_id}.items():
          setattr(vehicle_edited_record, key, value)
    db.commit()
    db.refresh(vehicle_edited_record)
    vehicle_edited_record = vehicle_edited_record.to_dict() 

    res = {
        'vehicle_edited_record': vehicle_edited_record,
    }
    return res

async def delete_vehicle_id(db: Session, id: int):

    vehicle_deleted = None
    record_to_delete = db.query(models.Vehicle).filter(models.Vehicle.id == id).first()

    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        vehicle_deleted = record_to_delete.to_dict() 

    res = {
        'vehicle_deleted': vehicle_deleted,
    }
    return res

async def get_parking_history(db: Session):

    parking_history_all = db.query(models.ParkingHistory).all()
    parking_history_all = [new_data.to_dict() for new_data in parking_history_all] if parking_history_all else parking_history_all

    res = {
        'parking_history_all': parking_history_all,
    }
    return res

async def get_parking_history_id(db: Session, id: int):

    parking_history_one = db.query(models.ParkingHistory).filter(models.ParkingHistory.id == id).first() 
    parking_history_one = parking_history_one.to_dict() if parking_history_one else parking_history_one

    res = {
        'parking_history_one': parking_history_one,
    }
    return res

async def post_parking_history(db: Session, raw_data: schemas.PostParkingHistory):
    id:str = raw_data.id
    created_at:str = raw_data.created_at
    vehicle_id:int = raw_data.vehicle_id
    parking_slot_id:int = raw_data.parking_slot_id
    clock_in:str = raw_data.clock_in
    clock_out:str = raw_data.clock_out
    total_amount:int = raw_data.total_amount


    record_to_be_added = {'id': id, 'created_at': created_at, 'vehicle_id': vehicle_id, 'parking_slot_id': parking_slot_id, 'clock_in': clock_in, 'clock_out': clock_out, 'total_amount': total_amount}
    new_parking_history = models.ParkingHistory(**record_to_be_added)
    db.add(new_parking_history)
    db.commit()
    db.refresh(new_parking_history)
    parking_history_inserted_record = new_parking_history.to_dict()

    res = {
        'parking_history_inserted_record': parking_history_inserted_record,
    }
    return res

async def put_parking_history_id(db: Session, raw_data: schemas.PutParkingHistoryId):
    id:str = raw_data.id
    created_at:str = raw_data.created_at
    vehicle_id:str = raw_data.vehicle_id
    parking_slot_id:str = raw_data.parking_slot_id
    clock_in:str = raw_data.clock_in
    clock_out:str = raw_data.clock_out
    total_amount:str = raw_data.total_amount


    parking_history_edited_record = db.query(models.ParkingHistory).filter(models.ParkingHistory.id == id).first()
    for key, value in {'id': id, 'created_at': created_at, 'vehicle_id': vehicle_id, 'parking_slot_id': parking_slot_id, 'clock_in': clock_in, 'clock_out': clock_out, 'total_amount': total_amount}.items():
          setattr(parking_history_edited_record, key, value)
    db.commit()
    db.refresh(parking_history_edited_record)
    parking_history_edited_record = parking_history_edited_record.to_dict() 

    res = {
        'parking_history_edited_record': parking_history_edited_record,
    }
    return res

async def delete_parking_history_id(db: Session, id: int):

    parking_history_deleted = None
    record_to_delete = db.query(models.ParkingHistory).filter(models.ParkingHistory.id == id).first()

    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        parking_history_deleted = record_to_delete.to_dict() 

    res = {
        'parking_history_deleted': parking_history_deleted,
    }
    return res

async def post_login(db: Session, raw_data: schemas.PostLogin):
    email:str = raw_data.email
    password:str = raw_data.password



    query = db.query(models.Users)
    query = query.filter(
        
        and_(
            models.Users.email == email,
            models.Users.password == password
        )
    )


    user_status = query.all()
    user_status = [new_data.to_dict() for new_data in user_status] if user_status else user_status

    res = {
        'user_status': user_status,
    }
    return res

async def post_signup(db: Session, raw_data: schemas.PostSignup):
    name:str = raw_data.name
    email:str = raw_data.email
    password:str = raw_data.password


    emailExist = db.query(models.Users).filter(models.Users.email == email).count() > 0

    

    try:
        if emailExist :
            raise Exception("status_code=400, detail=You entered invalid credentials.")
    except Exception as e:
        raise HTTPException(500, str(e))



    res = {
    }
    return res

