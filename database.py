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
              price TEXT,
              desc TEXT,
              cat TEXT,
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



    def save_dish(self, data: dict):
        with sqlite3.connect(self.path) as conn:
            conn.execute("""
             INSERT INTO dishes (name, price, description, category, portion_options)
             VALUES (?, ?, ?, ?, ?)
         """, (data["name"], data["price"], data["description"], data["cat"], data["portion"]))

    def get_list_dish(self):
        with sqlite3.connect(self.path) as conn:
            cursor = conn.cursor()
            result = conn.execute("SELECT * FROM Dishes")
            result.row_factory = sqlite3.Row
            data = result.fetchall()

