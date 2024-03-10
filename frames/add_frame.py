import sys
import customtkinter
import res.font_constants as fonts
from db_manager import DatabaseManager

class AddFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure((0, 1, 2, 3), weight=1)
        
        self.db_manager = DatabaseManager()
        
        self.frame_label = customtkinter.CTkLabel(self, text="Temp", font=fonts.ARIAL_H1)
        self.frame_label.grid(row=0, column=0, padx=8, pady=8, sticky="swe")
        self.frame_label._text.center
        
        self.refresh_btn = customtkinter.CTkButton(self, text="Update results", command=self.update_results, font=fonts.ARIAL_DEFAULT)
        self.refresh_btn.grid(row=1, column=0, padx=8, pady=0, sticky="nwe")
    
    def update_results(self):
        pass