from app.models.Categories import Category

class CategoryService:
    # Constructor method
    def __init__(self, db_service):
        self.db = db_service

    # Method to check if a category already exists
    def exists(self, name):
        query = "SELECT id FROM categories WHERE name = ? COLLATE NOCASE"
        res = self.db.fetch_one(query, (name,))
        return res is not None  # True if exists
    
    # Method that gets a category by ID and returns a Category object
    def get_category_by_id(self, category_id):
        query = "SELECT id, name FROM categories WHERE id = ?"
        row = self.db.fetch_one(query, (category_id,))
        if row:
            return Category(id=row[0], name=row[1])
        return None

    # Method that retrieves all categories and returns a list of Category objects
    def get_all_categories(self):
        query = "SELECT id, name FROM categories ORDER BY name"
        rows = self.db.fetch_all(query)
        return [Category(id=row[0], name=row[1]) for row in rows]

    # Method that inserts a category into categories table
    def create_category(self, name):
        # Validates if category exists or not
        if self.exists(name):
            print(f"Category '{name}' already exists.")
            return False

        # If not, then insert into DB
        query = "INSERT INTO categories (name) VALUES (?)"
        self.db.execute_query(query, (name,))
        print(f'Category "{name}" created successfully.')
        return True

    # Method that updates a category name
    def update_category(self, category_id, new_name):
        # check if category_id exists
        if not self.get_category_by_id(category_id):
            print(f"Error: category ID {category_id} does not exist.")
            return False

        # check if new name already exists
        if self.exists(new_name):
            print(f"Error: category '{new_name}' already exists.")
            return False

        query = "UPDATE categories SET name = ? WHERE id = ?"
        self.db.execute_query(query, (new_name, category_id))

        print(f"Category ID {category_id} updated to '{new_name}'.")
        return True

    # Method that deletes a category from table
    def delete_category(self, category_id):
        if not self.get_category_by_id(category_id):
            print(f"Error: category ID {category_id} does not exist.")
            return False

        query = "DELETE FROM categories WHERE id = ?"
        self.db.execute_query(query, (category_id,))

        print(f"Category ID {category_id} deleted.")
        return True
