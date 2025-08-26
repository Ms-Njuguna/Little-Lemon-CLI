# imports
import click
from db import SessionLocal
from models import Customer, Table, Reservation
from tabulate import tabulate
from datetime import datetime

session = SessionLocal()