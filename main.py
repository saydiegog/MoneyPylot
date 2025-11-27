# main.py
# Entry point for the MoneyPylot application.
# Handles database initialization and simple console menu.

import os
from app.database.DatabaseService import DatabaseService
from app.database.CreateTables import create_tables
from app.services.CategoryService import CategoryService

DB_PATH = "app/database/moneypylot.db"


def initialize_database():
    """
    Ensures that the database file and tables exist.
    If the file does not exist, it is created.
    Tables are always validated using CREATE TABLE IF NOT EXISTS.
    """
    db_exists = os.path.exists(DB_PATH)

    if not db_exists:
        print("[INFO] Database not found. Creating new database...")
        create_tables(DB_PATH)
    else:
        print("[INFO] Database found.")

        # Even if DB exists, ensure tables exist
        print("[INFO] Validating table structure...")
        create_tables(DB_PATH)

    print("[INFO] Database initialization complete.")


def main_menu(category_service):
    """
    Displays the main console menu and routes user input.
    """
    while True:
        print("\n=== MoneyPylot Console Mode v0.0.1 ===")
        print("1. Create category")
        print("2. View all categories")
        print("3. Update category")
        print("4. Delete category")
        print("0. Exit")

        choice = input("\nSelect an option: ")

        if choice == "1":
            name = input("Enter category name: ")
            category_service.create_category(name)

        elif choice == "2":
            rows = category_service.get_all_categories()
            if not rows:
                print("No categories found.")
            else:
                print("\n--- Categories ---")
                for row in rows:
                    print(f"{row[0]} - {row[1]}")

        elif choice == "3":
            try:
                cat_id = int(input("Enter category ID to update: "))
                new_name = input("New name: ")
                category_service.update_category(cat_id, new_name)
            except ValueError:
                print("Invalid ID.")

        elif choice == "4":
            try:
                cat_id = int(input("Enter category ID to delete: "))
                category_service.delete_category(cat_id)
            except ValueError:
                print("Invalid ID.")

        elif choice == "0":
            print("Exiting MoneyPylot. Goodbye!")
            break

        else:
            print("Invalid option, try again.")


if __name__ == "__main__":
    print("=== MoneyPylot v0.0.1 ===")

    # Step 1: Initialize DB and tables
    initialize_database()

    # Step 2: Create database service
    db = DatabaseService(DB_PATH)

    # Step 3: Initialize services
    category_service = CategoryService(db)

    # Step 4: Start menu loop
    main_menu(category_service)
