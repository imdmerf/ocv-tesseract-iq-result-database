import sqlite3

class Database:
    def __init__(self, db_file):
        self.connection = sqlite3.connect ("data.db", timeout=10)
        self.cursor = self.connection.cursor()
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS persons (
                name TEXT,
                result INT
                )""")
        self.connection.commit()

    def add_person(self, word, iq_value):
        with self.connection:
            return self.cursor.execute("INSERT INTO 'persons' ('name', 'result') VALUES (?, ?)", (word, iq_value,))

    def database_verify(self):
        with self.connection:
            return self.cursor.execute("DELETE FROM persons WHERE result = 0")