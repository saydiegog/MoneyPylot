# main.py
# Clean, organized CLI for MoneyPylot.

import os
from app.database.create_tables import create_tables
from app.database.DatabaseService import DatabaseService
from app.services.CategoryService import CategoryService
from app.services.SubCategoryService import SubCategoryService
from app.services.IncomeService import IncomeService

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "app", "database", "moneypylot.db")


# ------------------------------------------------------------
#   DATABASE INIT
# ------------------------------------------------------------

def initialize_database():
    if not os.path.exists(DB_PATH):
        print("[INFO] Database not found. Creating new one...")
        create_tables()
    else:
        print("[INFO] Database found. Validating tables...")
        create_tables()

    print("[INFO] Database ready.\n")


# ------------------------------------------------------------
#   SUBMENUS
# ------------------------------------------------------------

def menu_categories():
    while True:
        print("\n=== CATEGORIES MENU ===")
        print("1. Create Category")
        print("2. List Categories")
        print("3. Update Category")
        print("4. Delete Category")
        print("5. View Subcategories of a Category")
        print("0. Back")
        choice = input("Select: ")

        if choice == "1":
            name = input("Category name: ")
            category_service.create_category(name)

        elif choice == "2":
            print("\n=== CATEGORIES ===")
            categories = category_service.get_all_categories()
            for c in categories:
                print(f"[{c.id}] {c.name}")

        elif choice == "3":
            cid = input("Category ID: ")
            new = input("New name: ")
            category_service.update_category(cid, new)

        elif choice == "4":
            cid = input("Category ID to delete: ")
            category_service.delete_category(cid)

        elif choice == "5":
            cid = input("Enter category ID: ")
            subs = subcategory_service.get_subcategories_by_category(cid)
            print("\n=== SUBCATEGORIES ===")
            for s in subs:
                print(f"[{s.id}] {s.name}")
            if not subs:
                print("No subcategories found.")

        elif choice == "0":
            return

        else:
            print("Invalid option.")


def menu_subcategories():
    while True:
        print("\n=== SUBCATEGORIES MENU ===")
        print("1. Create SubCategory")
        print("2. List All SubCategories")
        print("3. Update SubCategory")
        print("4. Delete SubCategory")
        print("0. Back")
        choice = input("Select: ")

        if choice == "1":
            name = input("Subcategory name: ")
            cid = input("Category ID: ")
            subcategory_service.create_subcategory(name, cid)

        elif choice == "2":
            subs = subcategory_service.get_all_subcategories()
            for s in subs:
                print(f"[{s.id}] {s.name} (Category {s.category_id})")

        elif choice == "3":
            sid = input("Subcategory ID: ")
            nn = input("New name: ")
            subcategory_service.update_subcategory(sid, nn)

        elif choice == "4":
            sid = input("Subcategory ID: ")
            subcategory_service.delete_subcategory(sid)

        elif choice == "0":
            return

        else:
            print("Invalid option.")


def menu_income():
    while True:
        print("\n=== INCOME MENU ===")
        print("1. Create Income")
        print("2. List All Incomes")
        print("3. Update Income")
        print("4. Delete Income")
        print("0. Back")
        choice = input("Select: ")

        if choice == "1":
            name = input("Income name: ")
            amount = float(input("Amount: "))
            recur = int(input("Recurring? (1 yes, 0 no): "))
            income_service.create_income(name, amount, recur)

        elif choice == "2":
            incomes = income_service.get_all_incomes()
            print("\n=== INCOME ===")
            for i in incomes:
                print(f"[{i.id}] {i.name} - ${i.amount} | recurring={i.is_recurring}")

        elif choice == "3":
            iid = input("Income ID: ")
            new = input("New name: ")
            amt = float(input("New amount: "))
            income_service.update_income(iid, new, amt)

        elif choice == "4":
            iid = input("Income ID: ")
            income_service.delete_income(iid)

        elif choice == "0":
            return

        else:
            print("Invalid option.")


# ------------------------------------------------------------
#   MAIN MENU
# ------------------------------------------------------------

def main():
    while True:
        print("\n=== MoneyPylot CLI v0.0.3 ===")
        print("1. Categories")
        print("2. SubCategories")
        print("3. Income")
        print("0. Exit")
        choice = input("Select option: ")

        if choice == "1":
            menu_categories()
        elif choice == "2":
            menu_subcategories()
        elif choice == "3":
            menu_income()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid option.")


# ------------------------------------------------------------
#   ENTRY POINT
# ------------------------------------------------------------

if __name__ == "__main__":
    initialize_database()

    db = DatabaseService(DB_PATH)

    # Services
    category_service = CategoryService(db)
    subcategory_service = SubCategoryService(db)
    income_service = IncomeService(db)

    main()
