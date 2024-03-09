import customtkinter
import res.font_constants as fonts
from frames.option_frame import OptionFrame
from db_manager import DatabaseManager

class CompareFrame(customtkinter.CTkFrame):
    def __init__(self, master, stats_frame):
        super().__init__(master)
        
        self.grid_columnconfigure((0, 1), weight=1)
        self.grid_rowconfigure((0, 2), weight=1)
        self.grid_rowconfigure(1, weight=7)
        
        self.db_manager = DatabaseManager()
        
        self.frame_title = customtkinter.CTkLabel(self, text="Compare", font=fonts.ARIAL_H1)
        self.frame_title.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="nwe")
        
        self.option_frame_1 = OptionFrame(self, 1, stats_frame)
        self.option_frame_1.grid(row=1, column=0, padx=(8, 4), pady=8, sticky="nswe")
        self.option_frame_2 = OptionFrame(self, 2, stats_frame)
        self.option_frame_2.grid(row=1, column=1, padx=(4, 8), pady=8, sticky="nswe")
        
        self.skip_btn = customtkinter.CTkButton(self, text="Skip", command=self.pair, font=fonts.ARIAL_DEFAULT)
        self.skip_btn.grid(row=2, column=0, columnspan=2, padx=64, pady=(10,10), sticky="nwe")
        
        self.pair()

    def pair(self):
        random_pairing = self.db_manager.execute_query('SELECT * FROM Pairings WHERE used = False ORDER BY RANDOM() LIMIT 1')
        
        self.option_frame_1.update(random_pairing[0])
        self.option_frame_2.update(random_pairing[0])
    