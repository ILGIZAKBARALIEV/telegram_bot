import sqlite3


class Database:
    def __init__(self, path: str):
        self.path = path

    def create_tables(self):
        with sqlite3.connect(self.path) as conn:
            conn.execute(
                """
                CREATE TABLE IF NOT EXISTS review (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    inst TEXT,
                    rate TEXT,
                    extra TEXT
    
                )
            """)
        conn.execute("""
        CREATE TABLE IF NOT EXISTS dish(
              id  INTEGER PRIMARY KEY AUTOINCREMENT,
              name TEXT,
              price INTEGER,
              description  TEXT,
              category TEXT,
              portion TEXT
              )
              """)

    def save_review(self, data: dict):
        with sqlite3.connect(self.path) as conn:
            conn.execute(
                """
                INSERT INTO review (name,inst,rate,extra)"""
                ,
                (data["name"], data["instagram_username"], data["rate"], data["extra"])
            )



    def  save_dish(self, data: dict):
        with sqlite3.connect(self.path) as conn:
            conn.execute("""
             INSERT INTO dish (
              name,
              price ,
              category,
              description,
              portion
              )
             VALUES (?, ?, ?, ?, ?)
         """, (data["name"], data["price"], data["category"], data["description"], data["portion"]))

    def get_list_dish(self):
        with sqlite3.connect(self.path) as conn:
            cursor = conn.cursor()
            result = conn.execute("SELECT * FROM Dish")
            result.row_factory = sqlite3.Row

            data = result.fetchall()
            return [dict(row) for row in data]

