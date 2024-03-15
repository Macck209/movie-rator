import customtkinter
import res.font_constants as fonts
from db_manager import DatabaseManager

class OptionFrame(customtkinter.CTkFrame):
    def __init__(self, master, frame_number, stats_frame):
        super().__init__(master)
        
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=4)
        self.grid_rowconfigure(1, weight=1)
        
        self.frame_number = frame_number
        if self.frame_number == 1:
            self.other_frame_number = 2
        else:
            self.other_frame_number = 1
        
        self.db_manager = DatabaseManager()
        self.stats_frame = stats_frame
        
        self.movie_title = customtkinter.CTkTextbox(self, font=fonts.ARIAL_DEFAULT, state="disabled", wrap="word", activate_scrollbars=False)
        self.movie_title.grid(row=0, column=0, padx=8, pady=8, sticky="nwes")
        self.movie_title.tag_config("center", justify="center", spacing1=96, spacing3=128)
        
        self.movie_btn = customtkinter.CTkButton(self, text="Better", command=self.selection, font=fonts.ARIAL_DEFAULT)
        self.movie_btn.grid(row=1, column=0, padx=8, pady=(0, 8), sticky="nswe")
    
    def update(self, pairing):
        self.pairing = pairing
        movie = self.db_manager.execute_query('SELECT * FROM Movies WHERE id = ?', (self.pairing[self.frame_number]))
        movie_title = movie[0][1]
        
        self.movie_title.configure(state="normal")
        self.movie_title.delete("0.0", "end")
        self.movie_title.insert("0.0", movie_title, "center")
        self.movie_title.configure(state="disabled")
        
    def selection(self):
        '''TODO reimplement later when all pairings are nearly exhausted
        if self.pairing == -1 or self.movie_score == -1:
            return'''
        
        self.db_manager.execute_query('UPDATE Pairings SET used = True WHERE id = ?', (self.pairing[0]))
        self.db_manager.execute_query('UPDATE Movies SET points = points + 1 WHERE id = ?', (self.pairing[self.frame_number]))
        self.db_manager.execute_query('UPDATE Movies SET points = points - 1 WHERE id = ?', (self.pairing[self.other_frame_number]))
        self.db_manager.execute_query('UPDATE Movies SET occurrences = occurrences + 1 WHERE id = ?', (self.pairing[self.frame_number]))
        self.db_manager.execute_query('UPDATE Movies SET occurrences = occurrences + 1 WHERE id = ?', (self.pairing[self.other_frame_number]))
        self.db_manager.execute_query('UPDATE Movies SET final_score = base_score + (points/occurrences) WHERE id = ?', (self.pairing[self.frame_number]))
        self.db_manager.execute_query('UPDATE Movies SET final_score = base_score + (points/occurrences) WHERE id = ?', (self.pairing[self.other_frame_number]))
        
        self.db_manager.update_ranking()
        self.stats_frame.update_stats()
        self.master.pair()