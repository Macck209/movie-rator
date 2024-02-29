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
        
        movies = self.db_manager.execute_query('SELECT * FROM Movies ORDER BY ranking LIMIT 100')
        
        for movie in movies:
            movie_title = movie[1]
            points = movie[2]
            occurrences = movie[3]
            ranking = movie[4]
            
            if ranking == 50:
                break
            '''elif occurrences == 0:
                continue'''
            
            label_text = f"{ranking} {movie_title}" #TODO {round(points/occurrences, 2)}
            
            self.label = customtkinter.CTkTextbox(self, font=fonts.ARIAL_DEFAULT_16, state="normal", wrap="char", activate_scrollbars=False, height=18)
            self.label.insert("0.0", label_text, "center")
            self.label.configure(state="disabled")
            self.label.pack(pady=2, expand=True, fill=tkinter.X)
    
    #TODO
    def update(self):
        pass