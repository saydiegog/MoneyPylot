from app.models.Expense import Expense

class ExpenseService:
    def __init__(self, db_service):
        self.db = db_service
    
    # Return an Expense object by ID
    def get_expense_by_id(self, expense_id):
        query = "SELECT id, subcategory_id, desc, amount, date FROM expenses WHERE id = ?"
        row = self.db.fetch_one(query, (expense_id,))
        if row:
            return Expense(id=row[0], subcategory_id=row[1], desc=row[2], amount=row[3], date=row[4])
        return None
    
    # Return all Expenses From certain Subcategory
    def get_all_subcategories(self, subcategory_id):
        query = "SELECT id, desc, amount, date FROM expenses WHERE subcategory_id = ? ORDER BY date"
        rows = self.db.fetch_all(query, (subcategory_id,))
        return [
            Expense(id=row[0], desc=row[1], amount=row[2], date=row[3]) 
            for row in rows
        ]
    
    # Insert a new Expense
    def create_expense(self, subcategory_id, desc, amount, date):

        query = "INSERT INTO subcategories (subcategory_id, desc, amount, date) VALUES (?, ?, ?, ?)"
        self.db.execute_query(query, (subcategory_id, desc, amount, date,))
        
        print(f'Expense "{desc, amount}" created successfully.')
        return True
    
    # Update Expense
    def update_subcategory(self, id, subcategory_id, desc, amount):
        
        exp = self.get_expense_by_id(id)
        if not exp:
            print(f"Error: Expense ID {id} does not exist.")
            return False

        query = "UPDATE expenses SET (subcategory_id = ?, desc = ?, amount = ?) WHERE id = ?"
        self.db.execute_query(query, (subcategory_id, desc, amount, id))

        print(f"Expense ID {subcategory_id} updated to Subcategory: '{subcategory_id}'  - Description: '{desc}' - Amount: '{amount}'.")
        return True
    
    # Delete an expense
    def delete_expense(self, id):

        if not self.get_expense_by_id(id):
            print(f"Error: Expense ID {id} does not exist.")
            return False

        query = "DELETE FROM expenses WHERE id = ?"
        self.db.execute_query(query, (id,))

        print(f"Expense ID {id} deleted.")
        return True
