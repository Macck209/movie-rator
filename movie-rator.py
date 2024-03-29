import customtkinter
from frames.compare_frame import CompareFrame
from frames.result_frame import ResultFrame
from frames.settings_frame import SettingsFrame
from frames.stats_frame import StatsFrame
from frames.search_frame import SearchFrame
from frames.add_frame import AddFrame

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        
        customtkinter.set_appearance_mode("Dark")
        customtkinter.set_default_color_theme("dark-blue")

        self.geometry("840x600")
        self.title("MovieRator")
        
        self.grid_columnconfigure((0, 2), weight=18)
        self.grid_columnconfigure(1, weight=24)
        self.grid_columnconfigure(3, weight=20)
        self.grid_rowconfigure((0, 1), weight=40)
        self.grid_rowconfigure(2, weight=30)
        self.grid_rowconfigure(3, weight=10)
        
        self.stats_frame = StatsFrame(self)
        self.stats_frame.grid(row=2, column=1, padx=(8, 0), pady=(0, 8), sticky="nswe", rowspan=2)
        
        self.compare_frame = CompareFrame(self, self.stats_frame)
        self.compare_frame.grid(row=0, column=0, padx=(8, 0), pady=8, sticky="nswe", rowspan=2, columnspan=3)
        
        self.add_frame = AddFrame(self)
        self.add_frame.grid(row=2, column=0, padx=(8, 0), pady=8, sticky="nswe", rowspan=2)
        
        self.result_frame = ResultFrame(self)
        self.result_frame.grid(row=0, column=3, padx=8, pady=8, sticky="nswe", rowspan=3)
        
        self.search_frame = SearchFrame(self, self.result_frame)
        self.search_frame.grid(row=3, column=3, padx=8, pady=(0, 8), sticky="nswe", rowspan=1)
        
        self.settings_frame = SettingsFrame(self, self.result_frame)
        self.settings_frame.grid(row=2, column=2, padx=(8, 0), pady=(0, 8), sticky="nswe", rowspan=2)
        
if __name__ == "__main__":
    app = App()
    app.mainloop()