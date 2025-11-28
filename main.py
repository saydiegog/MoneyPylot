# main.py
# Entry point for the MoneyPylot application.
# Handles database initialization and simple console menu.

import os
from app.database.create_tables import create_tables
from app.database.DatabaseService import DatabaseService
from app.services.CategoryService import CategoryService
from app.services.SubCategoryService import SubCategoryService

BASE_DIR = os.path.dirname(os.path.abspath(__file__))  
DB_PATH = os.path.join(BASE_DIR, "app", "database", "moneypylot.db")


def initialize_database():
    """
    Ensures that the database file and tables exist.
    If the file does not exist, it is created.
    Tables are always validated using CREATE TABLE IF NOT EXISTS.
    """
    db_exists = os.path.exists(DB_PATH)

    if not db_exists:
        print("[INFO] Database not found. Creating new database...")
        # this will create and initialize the DB
        create_tables()
    else:
        print("[INFO] Database found.")
        print("[INFO] Validating table structure...")
        # validate tables (CREATE IF NOT EXISTS)
        create_tables()

    print("[INFO] Database initialization complete.")


def print_menu():
    print("\n=== Expense Tracker CLI ===")
    print("1. Create Category")
    print("2. List Categories")
    print("3. Update Category")
    print("4. Delete Category")
    print("--------------------------------")
    print("5. Create SubCategory")
    print("6. List SubCategories")
    print("7. Update SubCategory")
    print("8. Delete SubCategory")
    print("--------------------------------")
    print("0. Exit")
    print("===============================")

def main():

    while True:
        print_menu()
        choice = input("Select option: ")

        # -------------------- CATEGORIES --------------------

        if choice == "1":
            name = input("Enter category name: ")
            category_service.create_category(name)

        elif choice == "2":
            print("\n=== CATEGORIES ===")
            categories = category_service.get_all_categories()
            for c in categories:
                print(f"[{c.id}] {c.name}")

        elif choice == "3":
            cat_id = input("Enter category ID to update: ")
            new_name = input("Enter new name: ")
            category_service.update_category(cat_id, new_name)

        elif choice == "4":
            cat_id = input("Enter category ID to delete: ")
            category_service.delete_category(cat_id)

        # -------------------- SUBCATEGORIES --------------------

        elif choice == "5":
            print("\n=== CREATE SUBCATEGORY ===")
            name = input("Subcategory name: ")
            category_id = input("Enter category ID it belongs to: ")

            subcategory_service.create_subcategory(name, category_id)

        elif choice == "6":
            print("\n=== SUBCATEGORIES ===")
            subcategories = subcategory_service.get_all_subcategories()
            for s in subcategories:
                print(f"[{s.id}] {s.name} (Category ID: {s.category_id})")

        elif choice == "7":
            print("\n=== UPDATE SUBCATEGORY ===")
            sub_id = input("Enter subcategory ID: ")
            new_name = input("New name: ")

            subcategory_service.update_subcategory(sub_id, new_name)

        elif choice == "8":
            print("\n=== DELETE SUBCATEGORY ===")
            sub_id = input("Enter subcategory ID: ")
            subcategory_service.delete_subcategory(sub_id)

        # -------------------- EXIT --------------------

        elif choice == "0":
            print("Exiting program...")
            break

        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    print("=== MoneyPylot v0.0.2 ===")
    print("=== DEBUG PATH CHECK ===")
    print("Base dir:", BASE_DIR)
    print("DB_PATH:", DB_PATH)
    print("Exists?:", os.path.exists(DB_PATH))
    print("========================")


    # Step 1: Initialize DB and tables
    initialize_database()

    # Step 2: Create database service
    db = DatabaseService(DB_PATH)

    # Step 3: Initialize services
    category_service = CategoryService(db)
    subcategory_service = SubCategoryService(db)

    # Step 4: Start menu loop
    main()
