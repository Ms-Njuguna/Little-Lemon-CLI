# imports
from sqlalchemy import Column, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from db import Base
from .reservation_customer import reservation_customer

class Reservation(Base):
    __tablename__ = "reservations"

    id = Column(Integer, primary_key=True)
    time = Column(DateTime, nullable=False)
    customer_id = Column(Integer, ForeignKey("customers.id"))
    table_id = Column(Integer, ForeignKey("tables.id"))

    customer = relationship("Customer", secondary=reservation_customer, back_populates="reservations")
    table = relationship("Table", back_populates="reservations")