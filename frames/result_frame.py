import tkinter
import customtkinter
import res.font_constants as fonts

class ResultFrame(customtkinter.CTkScrollableFrame):
    def __init__(self, master, movie_data):
        super().__init__(master)
        
        self.configure(label_fg_color="transparent")
        self.configure(label_text = "Top Movies")
        self.configure(label_font = fonts.ARIAL_H1)
        
        self.movie_data = movie_data
        
        for movie in self.movie_data["movies"]:
            movie_title = movie["movie_title"]
            ranking = movie["ranking"]
            points = movie["points"]
            occurrences = movie["occurrences"]
            
            if ranking == 50:
                break
            elif occurrences == 0:
                continue
            
            label_text = f"{ranking} {round(points/occurrences, 2)} {movie_title}"
            
            self.label = customtkinter.CTkTextbox(self, font=fonts.ARIAL_DEFAULT_16, state="normal", wrap="char", activate_scrollbars=False, height=18)
            self.label.insert("0.0", label_text, "center")
            self.label.configure(state="disabled")
            self.label.pack(pady=2, expand=True, fill=tkinter.X)