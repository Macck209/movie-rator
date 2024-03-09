import customtkinter
import res.font_constants as fonts
from db_manager import DatabaseManager
import threading
import time

class SearchFrame(customtkinter.CTkFrame):
    def __init__(self, master, result_frame):
        super().__init__(master)
        
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure((0, 1), weight=1)
        
        self.result_frame = result_frame
        self.db_manager = DatabaseManager()
        
        self.filter_entry = customtkinter.CTkEntry(self, placeholder_text="Movie title", font=fonts.ARIAL_DEFAULT)
        self.filter_entry.grid(row=0, column=0, padx=8, pady=(0,8), sticky="swe")
        self.filter_entry.configure(state="normal")
        self.filter_string = self.filter_entry.get()
        
        self.filter_btn = customtkinter.CTkButton(self, text="Filter results", command=self.filter_results, font=fonts.ARIAL_DEFAULT)
        self.filter_btn.grid(row=1, column=0, padx=8, pady=0, sticky="nwe")
        
        filter_thread = threading.Thread(target=self.filter_async)
        #filter_thread.start()
    
    def filter_async(self):
        while True:
            time.sleep(1)
            if self.filter_string != self.filter_entry.get():
                self.filter_entry.configure(state="disabled")
                self.filter_string = self.filter_entry.get()
                self.result_frame.update_ranking(self.filter_string, self.filter_entry)
        
    def filter_results(self):
        self.filter_entry.configure(state="disabled")
        self.result_frame.update_ranking(self.filter_entry.get())
        self.filter_entry.configure(state="normal")
    