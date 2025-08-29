# 🍋 Little Lemon CLI

A command-line interface (CLI) application for managing customers, tables, and reservations at the Little Lemon restaurant.
Built with Python, SQLAlchemy ORM, Alembic migrations, and Rich for terminal UI.

---

## Features
### Customer Management

- Add new customers with email and phone validation.
- View customer list in a clean table format.
- Update customer details.
- Delete customers from the database.

### Table Management

- Add tables with a number, capacity, and location (e.g., Patio, Window, Indoor).
- View all tables in a formatted table.
- Update table details (number, capacity, location).
- Delete tables.

### Reservation Management

- Book reservations for one or multiple customers.
- Assign tables and specify date/time.
- Optional fields: Occasion (e.g., Birthday, Anniversary) and Special Requests.
- Detects and prevents double-booking of tables.
- Suggests alternative available tables when conflicts occur.
- View all reservations with linked customers, tables, and details.
- Cancel reservations.

### Quick Searches

- Find customers by first or last name.
- Find reservations by date.

---

## Tech Stack

![Python](https://img.shields.io/badge/python-3.10%2B-blue?logo=python)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.0-red?logo=python)
![Alembic](https://img.shields.io/badge/Alembic-Migrations-green)
![Rich](https://img.shields.io/badge/Rich-Console_UI-purple)
![Questionary](https://img.shields.io/badge/Questionary-Interactive_CLI-orange)

---

## Project Structure

```bash

Little-Lemon-CLI/
├── alembic/                # Alembic migration setup
│   ├── versions/           # Migration scripts
│   └── env.py              # Alembic environment config
├── models/                 # Database models
│   ├── customer.py
│   ├── reservation.py
│   ├── reservation_customer.py
│   ├── table.py
│   └── __init__.py
├── cli.py                  # Main CLI entry point
├── db.py                   # Database connection & session
├── validators.py           # Input validation (email, phone)
├── little_lemon.db         # SQLite database file (auto-created)
├── alembic.ini             # Alembic config
├── Pipfile / Pipfile.lock  # Dependencies
└── README.md               # Project documentation

```

---

## Installation & Setup

1. Clone this repo
```bash

git clone https://github.com/yourusername/Little-Lemon-CLI.git
cd Little-Lemon-CLI

```

2. Install dependencies (using pipenv or pip)
```bash

pipenv install
pipenv shell

```

3. Run Alembic migrations (to set up the database schema)
```bash

alembic upgrade head

```

4. Start the CLI
```bash

python cli.py

```

---

## Demo Video

I recorded a Loom walkthrough explaining the code and showing the CLI in action:
![Watch the demo](https://drive.google.com/file/d/1__oGHmYxPacI2bEs9DFEXnqLej0aA-HO/view?usp=sharing)

---

## Usage
When you run the CLI, you’ll see the main menu:

```bash

🍋  Welcome to Little Lemon CLI  🍋

What would you like to do?
1. Manage customers
2. Manage tables
3. Manage reservations
4. Quick searches
---------------
Exit

```

From there you can:

   - Manage customers 
   - Manage tables 
   - Book or cancel reservations 
   - Search for customers/reservations 

---

## Future Improvements

- Export reservations/customers to CSV.
- Add authentication for staff.
- Advanced search & filtering.
- Support for PostgreSQL/MySQL.
- Reservation reminders via email/SMS

---

## License

This project is licensed under the MIT License.
Copyright (c) 2025 Ms-Njuguna