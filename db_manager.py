import sqlite3

class DatabaseManager:
    instance = None

    def __new__(cls):
        if not cls.instance:
            cls.instance = super(DatabaseManager, cls).__new__(cls)
            cls.instance.conn = sqlite3.connect('tests/series.db') # Enter your database path
            cls.instance.cursor = cls.instance.conn.cursor()
        return cls.instance

    def execute_query(self, query, *params):
        self.cursor.execute(query, params)
        self.conn.commit()
        return self.cursor.fetchall()
    
    def update_ranking(self):
        self.cursor.execute('''
    SELECT *, CASE WHEN occurrences = 0 THEN -1 ELSE final_score END AS ranked_score
    FROM Movies
    ORDER BY ranked_score DESC;
''')
        ordered_movies = self.cursor.fetchall()
        
        for index, movie in enumerate(ordered_movies, start=1):
            movie_id = movie[0]
            self.cursor.execute('UPDATE Movies SET ranking = ? WHERE id = ?', (index, movie_id))
        
        self.conn.commit()
    
    def close_connection(self):
        self.conn.close()