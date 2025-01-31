import sqlite3

class Database:
    def __init__(self, path: str):
        self.path = path

    def create_tables(self):
        with sqlite3.connect(self.path) as conn:
            # Создание таблицы для блюд
            conn.execute("""
                CREATE TABLE IF NOT EXISTS dish(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    price REAL,
                    description TEXT,
                    category TEXT,
                    portion TEXT,
                    photo TEXT
                )
            """)

    def save_dish(self, data: dict):
        with sqlite3.connect(self.path) as conn:
            conn.execute("""
                INSERT INTO dish (name, price, category, description, portion, photo)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (data["name"], data["price"], data["category"], data["description"], data["portion"], data.get("photo", "")))

    def get_list_dish(self, limit: int = 5, offset: int = 0):
        with sqlite3.connect(self.path) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM dish LIMIT ? OFFSET ?", (limit, offset))
            rows = cursor.fetchall()
            return [dict(zip([column[0] for column in cursor.description], row)) for row in rows]

    def get_total_dishes(self):
        with sqlite3.connect(self.path) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT COUNT(*) FROM dish')
            return cursor.fetchone()[0]
