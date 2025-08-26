# imports
import click
from db import SessionLocal
from models import Customer, Table, Reservation
from datetime import datetime
from rich.console import Console
from rich.table import Table as RichTable

session = SessionLocal()
console = Console()

# ----------CLI Welcome------------
@click.group()
def cli():
    """🍋  Welcome to Little Lemon CLI  🍋"""
    pass

if __name__ == "__main__":
    cli()