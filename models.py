from sqlalchemy.ext.declarative import as_declarative, declared_attr
from sqlalchemy.orm import class_mapper
import uuid
from datetime import datetime
from decimal import Decimal

from sqlalchemy import Column, Integer, String, Boolean, DateTime, Time, Float, Text, ForeignKey, JSON, Numeric, Date, \
    TIMESTAMP, UUID
from sqlalchemy.ext.declarative import declarative_base


@as_declarative()
class Base:
    id: int
    __name__: str

    # Auto-generate table name if not provided
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    # Generic to_dict() method
    def to_dict(self):
        """
        Converts the SQLAlchemy model instance to a dictionary, ensuring UUID fields are converted to strings.
        """
        result = {}
        for column in class_mapper(self.__class__).columns:
            value = getattr(self, column.key)
                # Handle UUID fields
            if isinstance(value, uuid.UUID):
                value = str(value)
            # Handle datetime fields
            elif isinstance(value, datetime):
                value = value.isoformat()  # Convert to ISO 8601 string
            # Handle Decimal fields
            elif isinstance(value, Decimal):
                value = float(value)

            result[column.key] = value
        return result




class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    created_at = Column(Date, primary_key=False)
    name = Column(String, primary_key=False)
    email = Column(String, primary_key=False)
    password = Column(String, primary_key=False)


class ParkingLots(Base):
    __tablename__ = 'parking_lots'
    id = Column(Integer, primary_key=True)
    created_at = Column(Date, primary_key=False)
    name = Column(String, primary_key=False)
    location = Column(String, primary_key=False)
    capacity = Column(Integer, primary_key=False)
    user_id = Column(Integer, primary_key=False)


class ParkingSlots(Base):
    __tablename__ = 'parking_slots'
    id = Column(Integer, primary_key=True)
    created_at = Column(Date, primary_key=False)
    type = Column(String, primary_key=False)
    is_occupied = Column(String, primary_key=False)
    price_per_hour = Column(Integer, primary_key=False)
    parking_lot_id = Column(Integer, primary_key=False)


class Vehicle(Base):
    __tablename__ = 'vehicle'
    id = Column(Integer, primary_key=True)
    created_at = Column(Date, primary_key=False)
    registration_id = Column(Integer, primary_key=False)
    owner_name = Column(String, primary_key=False)
    phone_number = Column(Integer, primary_key=False)
    model_type = Column(String, primary_key=False)
    color = Column(String, primary_key=False)
    parking_lot_id = Column(Integer, primary_key=False)
    parking_slot_id = Column(Integer, primary_key=False)


class ParkingHistory(Base):
    __tablename__ = 'parking_history'
    id = Column(Integer, primary_key=True)
    created_at = Column(Date, primary_key=False)
    vehicle_id = Column(Integer, primary_key=False)
    parking_slot_id = Column(Integer, primary_key=False)
    clock_in = Column(Date, primary_key=False)
    clock_out = Column(Date, primary_key=False)
    total_amount = Column(Integer, primary_key=False)


