import sqlite3
import customtkinter
from frames.setup_frames.confirm_frame import ConfirmFrame
from frames.setup_frames.import_frame import ImportFrame
from frames.setup_frames.input_frame import InputFrame

conn = sqlite3.connect('movies.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Movies (
        id INTEGER PRIMARY KEY,
        movie_title TEXT,
        points INTEGER,
        occurrences INTEGER,
        ranking INTEGER
    );
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Pairings (
        id INTEGER PRIMARY KEY,
        pair_first INTEGER,
        pair_second INTEGER,
        used BOOLEAN
    );
''')

conn.commit()
conn.close()

#TODO add first 2 movies

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        
        customtkinter.set_appearance_mode("Dark")
        customtkinter.set_default_color_theme("dark-blue")

        self.geometry("800x500")
        self.title("MovieRator - Setup")
        
        self.grid_columnconfigure((0, 1), weight=30)
        self.grid_columnconfigure(1, weight=40)
        self.grid_rowconfigure((0, 1), weight=40)
        self.grid_rowconfigure(2, weight=40)
        
        self.stats_frame = InputFrame(self)
        self.stats_frame.grid(row=0, column=0, padx=(8, 0), pady=8, sticky="nswe")
        
        self.compare_frame = ImportFrame(self)
        self.compare_frame.grid(row=0, column=1, padx=8, pady=8, sticky="nswe")
        
        self.result_frame = ConfirmFrame(self)
        self.result_frame.grid(row=1, column=0, padx=8, pady=(0, 8), sticky="nswe", columnspan=2)
        
if __name__ == "__main__":
    app = App()
    app.mainloop()