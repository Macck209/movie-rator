import tkinter
import customtkinter
import res.font_constants as fonts
from db_manager import DatabaseManager

class ResultFrame(customtkinter.CTkScrollableFrame):
    def __init__(self, master):
        super().__init__(master)
        
        self.configure(label_fg_color="transparent")
        self.configure(label_text = "Top Movies")
        self.configure(label_font = fonts.ARIAL_H1)
        
        self.db_manager = DatabaseManager()
        self.labels = []
        
        self.update_ranking()
    
    def update_ranking(self, filter_string=''):
        if filter_string != '':
            self.movies = self.db_manager.execute_query('SELECT * FROM Movies WHERE occurrences != 0 AND movie_title LIKE ? ORDER BY ranking', (f"%{filter_string}%"))
        else:
            self.movies = self.db_manager.execute_query('SELECT * FROM Movies WHERE occurrences != 0 ORDER BY ranking LIMIT 100')
        
        for label in self.labels:
            label.destroy()
        
        for movie in self.movies:
            movie_title = movie[1]
            #points = movie[2]
            occurrences = movie[3]
            ranking = movie[4]
            
            if occurrences == 0:
                continue
            
            label_text = f"{ranking} {movie_title}"
            
            label = customtkinter.CTkTextbox(self, font=fonts.ARIAL_DEFAULT_16, state="normal", wrap="char", activate_scrollbars=False, height=18)
            label.insert("0.0", label_text, "center")
            label.configure(state="disabled")
            label.pack(pady=2, expand=True, fill=tkinter.X)
            
            self.labels.append(label)