from app.models.Income import Income
import datetime

class IncomeService:
    # Constructor method
    def __init__(self, db_service):
        self.db = db_service
    
    # Method that gets a category by ID and returns a Category object
    def get_income_by_id(self, income_id):
        query = "SELECT * FROM income WHERE id = ?"
        row = self.db.fetch_one(query, (income_id,))
        if row:
            return Income(*row)
        return None

    # Method that retrieves all incomes and returns a list of Income objects
    def get_all_incomes(self):
        query = "SELECT * FROM income ORDER BY created_at DESC"
        rows = self.db.fetch_all(query)
        return [Income(*row) for row in rows]

    # Method that inserts a category into categories table
    def create_income(self, name, amount, is_recurring):
        query = f"INSERT INTO income (name, amount, is_recurring, created_at) VALUES (?, ?, ?, ?)"
        self.db.execute_query(query, (name, amount, is_recurring, datetime.now().isoformat()))
        print(f'Income "{name}: {amount}" added successfully.')
        return True

    # Method that updates an income
    def update_income(self, income_id, new_name, new_amount):
        # check if income_id exists
        if not self.get_income_by_id(income_id):
            print(f"Error: Income ID {income_id} does not exist.")
            return False

        query = "UPDATE income SET name = ?, amount = ? WHERE id = ?"
        self.db.execute_query(query, (new_name, new_amount, income_id))

        print(f"Income ID {income_id} updated to '{new_name}: {new_amount}'.")
        return True

    # Method that deletes an income from table
    def delete_income(self, income_id):
        if not self.get_income_by_id(income_id):
            print(f"Error: Income ID {income_id} does not exist.")
            return False

        query = "DELETE FROM income WHERE id = ?"
        self.db.execute_query(query, (income_id,))

        print(f"Income ID {income_id} deleted.")
        return True
