# imports
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from db import Base

class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email_address = Column(String, unique=True, nullable=False)
    phone_number = Column(String, unique=True, nullable=False)

    reservations = relationship("Reservation", back_populates="customer", cascade="all, delete-orphan")

    