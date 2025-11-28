# DatabaseService.py
# Provides a clean interface to interact with the SQLite database.
# Handles connections, query execution, and result fetching.

import sqlite3

class DatabaseService:
    # Constructor: runs automatically when creating an object
    def __init__(self, db_path):
        self.db_path = db_path
    
    # Private method that opens a connection to the DB
    def _connect(self):
        return sqlite3.connect(self.db_path)
        
    # Method to execute INSERT, UPDATE, DELETE
    def execute_query(self, query, params=None):
        conn = None
        try:
            conn = self._connect()  # opens DB connection
            cursor = conn.cursor()  # creates cursor for DB operations
            cursor.execute(query, params or ())  # executes query
            conn.commit()  # saves DB changes
        except sqlite3.Error as e:
            print(f'[Database Error]: {e}')
        finally:
            if conn:
                conn.close() #closes DB connection

    # Method that returns only one row
    def fetch_one(self, query, params=None):
        conn = None
        try:
            conn = self._connect()  # opens DB connection
            cursor = conn.cursor()
            cursor.execute(query, params or ())  
            res = cursor.fetchone()  # gets only one row
            return res
        
        except sqlite3.Error as e:
            print(f"[Database Error] {e}")
            return None
        
        finally:
            if conn:
                conn.close() #closes DB connection


    # Method that returns all rows from a query
    def fetch_all(self, query, params=None):
        conn = None
        try:
            conn = self._connect()
            cursor = conn.cursor()
            cursor.execute(query, params or ())  
            res = cursor.fetchall()  # gets all rows
            return res
        
        except sqlite3.Error as e:
            print(f"[Database Error] {e}")
            return []

        finally:
            if conn:
                conn.close() #closes DB connection
