import sys
import questionary # type: ignore
from rich.console import Console # type: ignore
from rich.table import Table as RichTable # type: ignore
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


# ---------------- Customers ----------------
def manage_customers():
    while True:
        console.print("\n[bold underline]Customer Management[/]\n", style="cyan")
        choice = questionary.select(
            "Choose an action:",
            choices=[
                "Add customer",
                "View customers",
                "Update customer",
                "Delete customer",
                "Back to main menu",
            ],
            qmark=""
        ).ask()

        if choice == "Add customer":
            first_name = questionary.text("Enter first name:").ask()
            last_name = questionary.text("Enter last name:").ask()
            email = questionary.text("Enter email address:").ask()
            phone = questionary.text("Enter phone number:").ask()
            customer = Customer(
                first_name=first_name,
                last_name=last_name,
                email_address=email,
                phone_number=phone
            )
            session.add(customer)
            session.commit()
            console.print(f"✅ Customer [bold]{first_name} {last_name}[/] added!", style="green")

        elif choice == "View customers":
            customers = session.query(Customer).all()
            table = RichTable(title="Customers")
            table.add_column("ID", justify="center")
            table.add_column("First Name", justify="left")
            table.add_column("Last Name", justify="left")
            table.add_column("Email", justify="left")
            table.add_column("Phone", justify="left")

            for c in customers:
                table.add_row(str(c.id), c.first_name, c.last_name, c.email_address, c.phone_number)

            console.print(table)

        elif choice == "Update customer":
            customers = session.query(Customer).all()
            if not customers:
                console.print("❌ No customers found.", style="red")
                continue
            options = [f"{c.id}. {c.first_name} {c.last_name}" for c in customers]
            selected = questionary.select("Select customer to update:", choices=options, qmark="").ask()
            cust_id = int(selected.split(".")[0])
            customer = session.query(Customer).get(cust_id)
            customer.first_name = questionary.text("Enter new first name:", default=customer.first_name).ask()
            customer.last_name = questionary.text("Enter new last name:", default=customer.last_name).ask()
            customer.email_address = questionary.text("Enter new email:", default=customer.email_address).ask()
            customer.phone_number = questionary.text("Enter new phone:", default=customer.phone_number).ask()
            session.commit()
            console.print("✅ Customer updated!", style="green")

        elif choice == "Delete customer":
            customers = session.query(Customer).all()
            if not customers:
                console.print("❌ No customers found.", style="red")
                continue
            options = [f"{c.id}. {c.first_name} {c.last_name}" for c in customers]
            selected = questionary.select("Select customer to delete:", choices=options, qmark="").ask()
            cust_id = int(selected.split(".")[0])
            customer = session.query(Customer).get(cust_id)
            session.delete(customer)
            session.commit()
            console.print("🗑️ Customer deleted!", style="red")

        elif choice == "Back to main menu":
            break


# ---------------- Tables ----------------
def manage_tables():
    while True:
        console.print("\n[bold underline]Table Management[/]\n", style="cyan")
        choice = questionary.select(
            "Choose an action:",
            choices=[
                "Add table",
                "View tables",
                "Update table",
                "Delete table",
                "Back to main menu",
            ],
            qmark=""
        ).ask()

        if choice == "Add table":
            table_number = int(questionary.text("Enter table number:").ask())
            capacity = int(questionary.text("Enter table capacity:").ask())
            table = Table(table_number=table_number, capacity=capacity)
            session.add(table)
            session.commit()
            console.print(f"✅ Table {table_number} (capacity {capacity}) added!", style="green")

        elif choice == "View tables":
            tables = session.query(Table).all()
            table_view = RichTable(title="Tables")
            table_view.add_column("ID", justify="center")
            table_view.add_column("Table Number", justify="center")
            table_view.add_column("Capacity", justify="center")

            for t in tables:
                table_view.add_row(str(t.id), str(t.table_number), str(t.capacity))

            console.print(table_view)

        elif choice == "Update table":
            tables = session.query(Table).all()
            if not tables:
                console.print("❌ No tables found.", style="red")
                continue
            options = [f"{t.id}. Table {t.table_number} (Capacity {t.capacity})" for t in tables]
            selected = questionary.select("Select table to update:", choices=options, qmark="").ask()
            table_id = int(selected.split(".")[0])
            table = session.query(Table).get(table_id)
            table.table_number = int(questionary.text("Enter new table number:", default=str(table.table_number)).ask())
            table.capacity = int(questionary.text("Enter new capacity:", default=str(table.capacity)).ask())
            session.commit()
            console.print("✅ Table updated!", style="green")

        elif choice == "Delete table":
            tables = session.query(Table).all()
            if not tables:
                console.print("❌ No tables found.", style="red")
                continue
            options = [f"{t.id}. Table {t.table_number}" for t in tables]
            selected = questionary.select("Select table to delete:", choices=options, qmark="").ask()
            table_id = int(selected.split(".")[0])
            table = session.query(Table).get(table_id)
            session.delete(table)
            session.commit()
            console.print("🗑️ Table deleted!", style="red")

        elif choice == "Back to main menu":
            break


# ---------------- Reservations ----------------
def manage_reservations():
    while True:
        console.print("\n[bold underline]Reservation Management[/]\n", style="cyan")
        choice = questionary.select(
            "Choose an action:",
            choices=[
                "Book reservation",
                "View reservations",
                "Cancel reservation",
                "Delete reservation",
                "Back to main menu",
            ],
            qmark=""
        ).ask()

        if choice == "Book reservation":
            customers = session.query(Customer).all()
            tables = session.query(Table).all()
            if not customers or not tables:
                console.print("❌ Need at least 1 customer and 1 table.", style="red")
                continue
            cust_choice = questionary.select(
                "Select customer:", choices=[f"{c.id}. {c.first_name} {c.last_name}" for c in customers], qmark=""
            ).ask()
            table_choice = questionary.select(
                "Select table:", choices=[f"{t.id}. Table {t.table_number} (Capacity {t.capacity})" for t in tables], qmark=""
            ).ask()
            date_str = questionary.text("Enter date & time (YYYY-MM-DD HH:MM):").ask()
            time = datetime.strptime(date_str, "%Y-%m-%d %H:%M")

            cust_id = int(cust_choice.split(".")[0])
            table_id = int(table_choice.split(".")[0])
            reservation = Reservation(customer_id=cust_id, table_id=table_id, time=time)
            session.add(reservation)
            session.commit()
            console.print("✅ Reservation booked!", style="green")

        elif choice == "View reservations":
            reservations = session.query(Reservation).all()
            table = RichTable(title="Reservations")
            table.add_column("ID", justify="center")
            table.add_column("Customer", justify="left")
            table.add_column("Table", justify="center")
            table.add_column("Time", justify="left")

            for r in reservations:
                cust = session.query(Customer).get(r.customer_id)
                tbl = session.query(Table).get(r.table_id)
                table.add_row(str(r.id), f"{cust.first_name} {cust.last_name}", str(tbl.table_number), r.time.strftime("%Y-%m-%d %H:%M"))

            console.print(table)

        elif choice == "Cancel reservation" or choice == "Delete reservation":
            reservations = session.query(Reservation).all()
            if not reservations:
                console.print("❌ No reservations found.", style="red")
                continue
            options = [f"{r.id}. {r.time.strftime('%Y-%m-%d %H:%M')}" for r in reservations]
            selected = questionary.select("Select reservation:", choices=options, qmark="").ask()
            res_id = int(selected.split(".")[0])
            reservation = session.query(Reservation).get(res_id)
            session.delete(reservation)
            session.commit()
            console.print("🗑️ Reservation removed!", style="red")

        elif choice == "Back to main menu":
            break

# ---------------- Searches ----------------
def manage_searches():
    while True:
        console.print("\n[bold underline]Quick Searches[/]\n", style="cyan")
        choice = questionary.select(
            "Choose a search option:",
            choices=[
                "Find customer by name",
                "Find reservations by date",
                "Back to main menu",
            ],
            qmark=""
        ).ask()

        if choice == "Find customer by name":
            name = questionary.text("Enter customer first or last name:").ask()
            customers = session.query(Customer).filter(
                (Customer.first_name.like(f"%{name}%")) | (Customer.last_name.like(f"%{name}%"))
            ).all()
            if not customers:
                console.print("❌ No customers found.", style="red")
            else:
                table = RichTable(title=f"Search Results for '{name}'")
                table.add_column("ID", justify="center")
                table.add_column("First Name", justify="left")
                table.add_column("Last Name", justify="left")
                table.add_column("Email", justify="left")
                table.add_column("Phone", justify="left")
                for c in customers:
                    table.add_row(str(c.id), c.first_name, c.last_name, c.email_address, c.phone_number)
                console.print(table)

        elif choice == "Find reservations by date":
            date_str = questionary.text("Enter date (YYYY-MM-DD):").ask()
            try:
                target_date = datetime.strptime(date_str, "%Y-%m-%d").date()
                reservations = session.query(Reservation).all()
                results = [r for r in reservations if r.time.date() == target_date]
                if not results:
                    console.print("❌ No reservations found.", style="red")
                else:
                    table = RichTable(title=f"Reservations on {date_str}")
                    table.add_column("ID", justify="center")
                    table.add_column("Customer", justify="left")
                    table.add_column("Table", justify="center")
                    table.add_column("Time", justify="left")
                    for r in results:
                        cust = session.query(Customer).get(r.customer_id)
                        tbl = session.query(Table).get(r.table_id)
                        table.add_row(str(r.id), f"{cust.first_name} {cust.last_name}", str(tbl.table_number), r.time.strftime("%Y-%m-%d %H:%M"))
                    console.print(table)
            except ValueError:
                console.print("❌ Invalid date format!", style="red")

        elif choice == "Back to main menu":
            break


if __name__ == "__main__":
    main_menu()
