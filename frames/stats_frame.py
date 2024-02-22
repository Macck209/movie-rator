import customtkinter
import res.font_constants as fonts

class StatsFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure((0, 1, 2, 3,4), weight=1)
        
        self.frame_label = customtkinter.CTkLabel(self, text="Stats", font=fonts.ARIAL_H1)
        self.frame_label.grid(row=0, column=0, padx=10, pady=10, sticky="swe")
        self.frame_label._text.center
        
        self.comparisons_label = customtkinter.CTkLabel(self, text="0/X comparisons", font=fonts.ARIAL_DEFAULT_16)
        self.comparisons_label.grid(row=1, column=0, padx=8, pady=0, sticky="nwe")
        self.movies_label = customtkinter.CTkLabel(self, text="X movies", font=fonts.ARIAL_DEFAULT_16)
        self.movies_label.grid(row=2, column=0, padx=8, pady=0, sticky="nwe")
        self.other_label = customtkinter.CTkLabel(self, text="soon", font=fonts.ARIAL_DEFAULT_16)
        self.other_label.grid(row=3, column=0, padx=8, pady=0, sticky="nwe")
        self.other_label_2 = customtkinter.CTkLabel(self, text="soon", font=fonts.ARIAL_DEFAULT_16)
        self.other_label_2.grid(row=4, column=0, padx=8, pady=(0,10), sticky="nwe")
    