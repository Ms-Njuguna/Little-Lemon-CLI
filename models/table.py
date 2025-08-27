# imports
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from db import Base

class Table(Base):
    __tablename__ = "tables"

    id = Column(Integer, primary_key=True)
    table_number = Column(Integer, unique=True, nullable=False)
    capacity = Column(Integer, nullable=False)
    location = Column(String, nullable=True)

    reservations = relationship("Reservation", back_populates="table", cascade="all, delete-orphan")