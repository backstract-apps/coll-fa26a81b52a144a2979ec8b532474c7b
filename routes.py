from fastapi import APIRouter, Request, Depends, HTTPException, UploadFile, Form
from sqlalchemy.orm import Session
from typing import List
import service, models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get('/users/')
async def get_users(db: Session = Depends(get_db)):
    try:
        return await service.get_users(db)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/users/id')
async def get_users_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_users_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/users/')
async def post_users(raw_data: schemas.PostUsers, db: Session = Depends(get_db)):
    try:
        return await service.post_users(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/users/id/')
async def put_users_id(raw_data: schemas.PutUsersId, db: Session = Depends(get_db)):
    try:
        return await service.put_users_id(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/users/id')
async def delete_users_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_users_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/parking_lots/')
async def get_parking_lots(db: Session = Depends(get_db)):
    try:
        return await service.get_parking_lots(db)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/parking_lots/id')
async def get_parking_lots_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_parking_lots_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/parking_lots/')
async def post_parking_lots(raw_data: schemas.PostParkingLots, db: Session = Depends(get_db)):
    try:
        return await service.post_parking_lots(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/parking_lots/id/')
async def put_parking_lots_id(raw_data: schemas.PutParkingLotsId, db: Session = Depends(get_db)):
    try:
        return await service.put_parking_lots_id(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/parking_lots/id')
async def delete_parking_lots_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_parking_lots_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/parking_slots/')
async def get_parking_slots(db: Session = Depends(get_db)):
    try:
        return await service.get_parking_slots(db)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/parking_slots/id')
async def get_parking_slots_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_parking_slots_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/parking_slots/')
async def post_parking_slots(raw_data: schemas.PostParkingSlots, db: Session = Depends(get_db)):
    try:
        return await service.post_parking_slots(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/parking_slots/id/')
async def put_parking_slots_id(raw_data: schemas.PutParkingSlotsId, db: Session = Depends(get_db)):
    try:
        return await service.put_parking_slots_id(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/parking_slots/id')
async def delete_parking_slots_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_parking_slots_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/vehicle/')
async def get_vehicle(db: Session = Depends(get_db)):
    try:
        return await service.get_vehicle(db)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/vehicle/id')
async def get_vehicle_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_vehicle_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/vehicle/')
async def post_vehicle(raw_data: schemas.PostVehicle, db: Session = Depends(get_db)):
    try:
        return await service.post_vehicle(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/vehicle/id/')
async def put_vehicle_id(raw_data: schemas.PutVehicleId, db: Session = Depends(get_db)):
    try:
        return await service.put_vehicle_id(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/vehicle/id')
async def delete_vehicle_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_vehicle_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/parking_history/')
async def get_parking_history(db: Session = Depends(get_db)):
    try:
        return await service.get_parking_history(db)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/parking_history/id')
async def get_parking_history_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_parking_history_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/parking_history/')
async def post_parking_history(raw_data: schemas.PostParkingHistory, db: Session = Depends(get_db)):
    try:
        return await service.post_parking_history(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/parking_history/id/')
async def put_parking_history_id(raw_data: schemas.PutParkingHistoryId, db: Session = Depends(get_db)):
    try:
        return await service.put_parking_history_id(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/parking_history/id')
async def delete_parking_history_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_parking_history_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/login')
async def post_login(raw_data: schemas.PostLogin, db: Session = Depends(get_db)):
    try:
        return await service.post_login(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/signup')
async def post_signup(raw_data: schemas.PostSignup, db: Session = Depends(get_db)):
    try:
        return await service.post_signup(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

