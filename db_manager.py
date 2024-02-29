import sqlite3

class DatabaseManager:
    instance = None

    def __new__(cls):
        if not cls.instance:
            cls.instance = super(DatabaseManager, cls).__new__(cls)
            cls.instance.conn = sqlite3.connect('movies.db')
            cls.instance.cursor = cls.instance.conn.cursor()
        return cls.instance

    def execute_query(self, query, *params):
        self.cursor.execute(query, params)
        self.conn.commit()
        return self.cursor.fetchall()
    
    def close_connection(self):
        self.conn.close()