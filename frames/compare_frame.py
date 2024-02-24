import customtkinter
import random
import res.font_constants as fonts
from frames.option_frame import OptionFrame

class CompareFrame(customtkinter.CTkFrame):
    def __init__(self, master, pairing_data, movie_data):
        super().__init__(master)
        
        self.pairing_data = pairing_data
        self.movie_data = movie_data
        
        self.grid_columnconfigure((0, 1), weight=1)
        self.grid_rowconfigure((0, 2), weight=1)
        self.grid_rowconfigure(1, weight=7)
        
        self.frame_title = customtkinter.CTkLabel(self, text="Compare", font=fonts.ARIAL_H1)
        self.frame_title.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="nwe")
        
        self.option_frame_1 = OptionFrame(self, pairing_data)
        self.option_frame_1.grid(row=1, column=0, padx=(8, 4), pady=8, sticky="nswe")
        self.option_frame_2 = OptionFrame(self, pairing_data)
        self.option_frame_2.grid(row=1, column=1, padx=(4, 8), pady=8, sticky="nswe")
        
        self.test_btn = customtkinter.CTkButton(self, text="Skip", command=self.pair, font=fonts.ARIAL_DEFAULT)
        self.test_btn.grid(row=2, column=0, columnspan=2, padx=64, pady=(10,10), sticky="nwe")
        
        self.pair()

    def pair(self):
        random_pairing = next(random.choice(self.pairing_data["pairings"]) for pair in self.pairing_data["pairings"] if pair["used"] == False)

        movie_1_id, movie_2_id = random_pairing["pair"]
        movie_1 = next(movie for movie in self.movie_data["movies"] if movie["id"] == movie_1_id)
        movie_2 = next(movie for movie in self.movie_data["movies"] if movie["id"] == movie_2_id)
        
        movie_1_title = movie_1["movie_title"]
        movie_2_title = movie_2["movie_title"]
        
        self.option_frame_1.update(f"{movie_1_title}", random_pairing, movie_1, movie_2)
        self.option_frame_2.update(f"{movie_2_title}", random_pairing, movie_2, movie_1)
    