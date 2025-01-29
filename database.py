import sqlite3

class Database:
    def __init__(self,path:str):
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
    def save_review(self, data:dict):
        with sqlite3.connect(self.path) as conn:
            conn.execute(
                """
                INSERT INTO review (name,inst,rate,extra)"""
            ,
                (data["name"],data["instagram_username"],data["rate"],data["extra"])
            )

    def save_dish(self,data:dict):
        with sqlite3.connect(self.path) as conn:
            conn.execute("""
            INSERT INTO dishes (name, price, description, category, portion_options)
            VALUES (?, ?, ?, ?, ?)
        """, (data["name"], data["price"], data["description"], data["cat"], data["portion"]))


    def list_dish(self,data:dict):
        with sqlite3.connect(self.path) as conn:
            conn.execute("""
            INSERT INTO dishes (name, price, description, category, portion_options)
            VALUES (?, ?, ?, ?, ?)
        """, (data["name"], data["price"], data["description"], data["cat"], data["portion"]))

class Database:
    def __init__(self, db_path):
        self.db_path = db_path
        self.connection = sqlite3.connect(self.db_path)
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS dishes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            price TEXT,
            description TEXT,
            category TEXT,
            portion TEXT
        )
        """)
        self.connection.commit()

    def save_dish(self, data):
        self.cursor.execute("INSERT INTO dishes (name, price, description, category, portion) VALUES (?, ?, ?, ?, ?)",
                            (data['name'], data['price'], data['desc'], data['cat'], data['portion']))
        self.connection.commit()

    def get_all_dishes(self):
        self.cursor.execute("SELECT name, price, description, category, portion FROM dishes")
        rows = self.cursor.fetchall()
        return [{"name": row[0], "price": row[1], "description": row[2], "category": row[3], "portion": row[4]} for row in rows]

database = Database("bot_database.db")

