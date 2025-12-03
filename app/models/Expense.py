from datetime import datetime

class Expense:
    def __init__(self, id, subcategory_id, desc, amount, date):
        self.id = id
        self.subcategory_id = subcategory_id
        self.desc = desc
        self.amount = amount 
        if isinstance(date, datetime):
            self.date = date
        else:
            self.date = datetime.fromisoformat(date)