import sqlite3
from pathlib import Path
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "moneypylot.db")

def create_tables():
    """Creates all required tables for the MVP of MoneyPylot."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Enable foreign key constraint enforcement
    cursor.execute("PRAGMA foreign_keys = ON;")

    # Table: income
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS income (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            amount REAL NOT NULL,
            is_recurring INTEGER NOT NULL CHECK (is_recurring IN (0, 1)),
            created_at TEXT NOT NULL
        );
    """)

    # Table: categories
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS categories (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE
        );
    """)

    # Table: subcategories
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS subcategories (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            category_id INTEGER NOT NULL,
            name TEXT NOT NULL,
            FOREIGN KEY (category_id) REFERENCES categories(id) ON DELETE CASCADE
        );
    """)

    # Table: expenses
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            subcategory_id INTEGER NOT NULL,
            description TEXT NOT NULL,
            amount REAL NOT NULL,
            date TEXT NOT NULL,
            FOREIGN KEY (subcategory_id) REFERENCES subcategories(id)
        );
    """)

    # Table: recurring_expenses
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS recurring_expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            subcategory_id INTEGER NOT NULL,
            description TEXT NOT NULL,
            amount REAL NOT NULL,
            period TEXT NOT NULL, 
            start_date TEXT NOT NULL,
            end_date TEXT,
            FOREIGN KEY (subcategory_id) REFERENCES subcategories(id)
        );
    """)

    conn.commit()
    conn.close()

    print("✔️ All tables created successfully.")


if __name__ == "__main__":
    create_tables()
