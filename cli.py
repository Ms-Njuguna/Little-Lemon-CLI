import sys
import questionary
from rich.console import Console
from rich.table import Table as RichTable
from db import SessionLocal
from models import Customer, Table, Reservation
from datetime import datetime

session = SessionLocal()
console = Console()


def main_menu():
    console.print("\n🍋  Welcome to Little Lemon CLI  🍋\n")

    while True:
        choice = questionary.select(
            "What would you like to do?",
            choices=[
                "1. Manage customers",
                "2. Manage tables",
                "3. Manage reservations",
                "4. Quick searches",
                questionary.Separator(),
                "Exit",
            ],
            qmark=""   # remove the "?"
        ).ask()

        if choice == "1. Manage customers":
            manage_customers()
        elif choice == "2. Manage tables":
            manage_tables()
        elif choice == "3. Manage reservations":
            manage_reservations()
        elif choice == "4. Quick searches":
            manage_searches()
        elif choice == "Exit":
            console.print("\n🍋  Thank you for using Little Lemon CLI. Goodbye! 🍋\n")
            sys.exit(0)




if __name__ == "__main__":
    main_menu()
