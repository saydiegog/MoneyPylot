from datetime import datetime

class Income:
    def __init__(self, id, name, amount, is_recurring, created_at):
        self.id = id
        self.name = name
        self.amount = amount 
        self.is_recurring = is_recurring
        self.created_at = datetime.fromisoformat(created_at)