import customtkinter
import res.font_constants as fonts
from db_manager import DatabaseManager

class StatsFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure((0, 1, 2, 3,4), weight=1)
        
        self.db_manager = DatabaseManager()
        
        self.frame_label = customtkinter.CTkLabel(self, text="Stats", font=fonts.ARIAL_H1)
        self.frame_label.grid(row=0, column=0, padx=10, pady=10, sticky="swe")
        self.frame_label._text.center
        
        self.total_comparisons = self.db_manager.execute_query('SELECT COUNT(*) FROM Pairings')[0][0]
        self.comparisons = self.db_manager.execute_query('SELECT COUNT(*) FROM Pairings WHERE used = True')[0][0]
        self.total_movies = self.db_manager.execute_query('SELECT COUNT(*) FROM Movies')[0][0]
        self.best_movie = self.db_manager.execute_query('SELECT * FROM Movies WHERE ranking = (SELECT MIN(ranking) FROM Movies) LIMIT 1')[0][1]
        self.worst_movie = self.db_manager.execute_query('SELECT * FROM Movies WHERE ranking = (SELECT MAX(ranking) FROM Movies) LIMIT 1')[0][1]
        
        self.comparisons_label = customtkinter.CTkLabel(self, text=f"Comparisons: {self.comparisons} / {self.total_comparisons}", font=fonts.ARIAL_DEFAULT_16)
        self.comparisons_label.grid(row=1, column=0, padx=8, pady=0, sticky="nwe")
        self.movies_label = customtkinter.CTkLabel(self, text=f"Movies: {self.total_movies}", font=fonts.ARIAL_DEFAULT_16)
        self.movies_label.grid(row=2, column=0, padx=8, pady=0, sticky="nwe")
        self.best_movie_label = customtkinter.CTkLabel(self, text=f"Best movie: {self.best_movie}", font=fonts.ARIAL_DEFAULT_16)
        self.best_movie_label.grid(row=3, column=0, padx=8, pady=0, sticky="nwe")
        self.worst_movie_label = customtkinter.CTkLabel(self, text=f"Worst movie: {self.worst_movie}", font=fonts.ARIAL_DEFAULT_16)
        self.worst_movie_label.grid(row=4, column=0, padx=8, pady=(0,10), sticky="nwe")
    
    def update_stats(self):
        self.total_comparisons = self.db_manager.execute_query('SELECT COUNT(*) FROM Pairings')[0][0]
        self.comparisons = self.db_manager.execute_query('SELECT COUNT(*) FROM Pairings WHERE used = True')[0][0]
        self.best_movie = self.db_manager.execute_query('SELECT * FROM Movies WHERE ranking = (SELECT MIN(ranking) FROM Movies) LIMIT 1')[0][1]
        self.worst_movie = self.db_manager.execute_query('SELECT * FROM Movies WHERE ranking = (SELECT MAX(ranking) FROM Movies) LIMIT 1')[0][1]
        
        self.comparisons_label.configure(text=f"Comparisons: {self.comparisons} / {self.total_comparisons}")
        self.best_movie_label.configure(text=f"Best movie: {self.best_movie}")
        self.worst_movie_label.configure(text=f"Worst movie: {self.worst_movie}")
    
    #TODO adding movies to database (new frame?)
    def update_movie_count(self):
        self.total_comparisons = self.db_manager.execute_query('SELECT COUNT(*) FROM Pairings')[0][0]
        self.comparisons = self.db_manager.execute_query('SELECT COUNT(*) FROM Pairings WHERE used = True')[0][0]
        self.total_movies = self.db_manager.execute_query('SELECT COUNT(*) FROM Movies')[0][0]
        
        self.comparisons_label.configure(text=f"Comparisons: {self.comparisons} / {self.total_comparisons}")
        self.movies_label.configure(text=f"Movies: {self.total_movies}")
