# database connection --> db.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "sqlite:///little_lemon.db"

engine = create_engine(DATABASE_URL, echo=False)
SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()


from models import Table, Customer, Reservation

# Create tables based on current models
Base.metadata.create_all(engine)