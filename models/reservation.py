# imports
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from db import Base

class Reservation(Base):
    __tablename__ = "reservations"

    id = Column(Integer, primary_key=True)
    time = Column(DateTime, nullable=False)
    customer_id = Column(Integer, ForeignKey("customers.id"))
    table_id = Column(Integer, ForeignKey("tables.id"))

    customer = relationship("Customer", back_populates="reservations")
    table = relationship("Table", back_populates="reservations")