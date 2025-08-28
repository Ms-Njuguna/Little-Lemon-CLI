# imports
from sqlalchemy import Column, Integer, DateTime, ForeignKey, String
from sqlalchemy.orm import relationship
from db import Base
from .reservation_customer import reservation_customer

class Reservation(Base):
    __tablename__ = "reservations"

    id = Column(Integer, primary_key=True)
    time = Column(DateTime, nullable=False)
    table_id = Column(Integer, ForeignKey("tables.id"))

    # optional inputs for the reservation
    occassion = Column(String, nullable=True)
    special_requests = Column(String, nullable=True)

    customers = relationship("Customer", secondary=reservation_customer, back_populates="reservations")
    table = relationship("Table", back_populates="reservations")