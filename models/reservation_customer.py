# imports
from sqlalchemy import Column, Integer, Table, ForeignKey
from db import Base

reservation_customer = Table(
    "reservation_customer",
    Base.metadata,
    Column("reservation_id", Integer, ForeignKey("reservations.id"), primary_key=True),
    Column("customer_id", Integer, ForeignKey("customers.id"), primary_key=True),
)