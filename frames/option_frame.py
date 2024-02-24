import customtkinter
import res.font_constants as fonts

class OptionFrame(customtkinter.CTkFrame):
    def __init__(self, master, pairing_data):
        super().__init__(master)
        
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=4)
        self.grid_rowconfigure(1, weight=1)
        
        self.pairing_data = pairing_data
        
        self.movie_title = customtkinter.CTkTextbox(self, font=fonts.ARIAL_DEFAULT, state="disabled", wrap="word", activate_scrollbars=False)
        self.movie_title.grid(row=0, column=0, padx=10, pady=10, sticky="nwes")
        self.movie_title.tag_config("center", justify="center", spacing1=96, spacing3=128)
        
        self.movie_btn = customtkinter.CTkButton(self, text="Better", command=self.selection, font=fonts.ARIAL_DEFAULT)
        self.movie_btn.grid(row=1, column=0, padx=10, pady=(0, 10), sticky="nswe")
    
    def update(self, movie_title, pairing, movie, other_movie):
        self.pairing = pairing
        self.movie = movie
        self.other_movie = other_movie
        
        self.movie_title.configure(state="normal")
        self.movie_title.delete("0.0", "end")
        self.movie_title.insert("0.0", movie_title, "center")
        self.movie_title.configure(state="disabled")
        
    def selection(self):
        '''TODO reimplement later when all pairings are nearly exhausted
        if self.pairing == -1 or self.movie_score == -1:
            return'''
        
        self.pairing["used"] = True
        self.movie["points"] +=1
        self.movie["occurrences"] +=1
        self.other_movie["occurrences"] +=1
        
        self.master.pair()