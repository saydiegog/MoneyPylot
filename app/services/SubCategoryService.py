from app.models.SubCategories import SubCategory

class SubCategoryService:
    def __init__(self, db_service):
        self.db = db_service
    
    # Check if subcategory already exists inside the same category
    def exists(self, name, category_id):
        query = """
            SELECT id FROM subcategories 
            WHERE name = ? AND category_id = ? COLLATE NOCASE
        """
        res = self.db.fetch_one(query, (name, category_id))
        return res is not None
    
    # Return a SubCategory object by ID
    def get_subcategory_by_id(self, subcategory_id):
        query = "SELECT id, category_id, name FROM subcategories WHERE id = ?"
        row = self.db.fetch_one(query, (subcategory_id,))
        if row:
            return SubCategory(id=row[0], category_id=row[1], name=row[2])
        return None
    
    # Return all subcategories
    def get_all_subcategories(self):
        query = "SELECT id, category_id, name FROM subcategories ORDER BY name"
        rows = self.db.fetch_all(query)
        return [
            SubCategory(id=row[0], category_id=row[1], name=row[2]) 
            for row in rows
        ]
    
    # Insert a subcategory
    def create_subcategory(self, name, category_id):
        
        if self.exists(name, category_id):
            print(f"SubCategory '{name}' already exists for that category.")
            return False

        query = "INSERT INTO subcategories (name, category_id) VALUES (?, ?)"
        self.db.execute_query(query, (name, category_id))
        
        print(f'SubCategory "{name}" created successfully.')
        return True
    
    # Update subcategory name
    def update_subcategory(self, subcategory_id, new_name):
        
        subcat = self.get_subcategory_by_id(subcategory_id)
        if not subcat:
            print(f"Error: SubCategory ID {subcategory_id} does not exist.")
            return False
        
        if self.exists(new_name, subcat.category_id):
            print(f"Error: subcategory '{new_name}' already exists.")
            return False

        query = "UPDATE subcategories SET name = ? WHERE id = ?"
        self.db.execute_query(query, (new_name, subcategory_id))

        print(f"SubCategory ID {subcategory_id} updated to '{new_name}'.")
        return True
    
    # Delete a subcategory
    def delete_subcategory(self, subcategory_id):
        
        if not self.get_subcategory_by_id(subcategory_id):
            print(f"Error: SubCategory ID {subcategory_id} does not exist.")
            return False

        query = "DELETE FROM subcategories WHERE id = ?"
        self.db.execute_query(query, (subcategory_id,))

        print(f"SubCategory ID {subcategory_id} deleted.")
        return True
