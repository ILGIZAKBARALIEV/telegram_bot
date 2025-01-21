import sqlite3

class Database:
    def __init__(self, path: str ):
        self.path = path

    def create_tables(self):
        with (sqlite3.connect(self.path) as
              conn:
                    cursor = conn.cursor()
                    conn.execute("""CREATE TABLE IF NOT EXISTS users (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                username TEXT,
                                digit INTEGER
                                review TEXT
                            )""")
