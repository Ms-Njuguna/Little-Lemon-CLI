# imports
from sqlalchemy import Column, Integer, ForeignKey, Table as SQLATable
from db import Base

reservation_customer = SQLATable(
    "reservation_customer",
    Base.metadata,
    Column("reservation_id", Integer, ForeignKey("reservations.id"), primary_key=True),
    Column("customer_id", Integer, ForeignKey("customers.id"), primary_key=True),
)