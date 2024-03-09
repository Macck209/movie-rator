import customtkinter
import res.font_constants as fonts

class InputFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        
        self.grid_columnconfigure((0, 1), weight=1)
        self.grid_rowconfigure((0, 2), weight=1)
        self.grid_rowconfigure(1, weight=7)
        
        self.frame_title = customtkinter.CTkLabel(self, text="Frame", font=fonts.ARIAL_H1)
        self.frame_title.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="nwe")
        
        self.test_btn = customtkinter.CTkButton(self, text="TempBtn", command=self.test, font=fonts.ARIAL_DEFAULT)
        self.test_btn.grid(row=2, column=0, columnspan=2, padx=64, pady=(10,10), sticky="nwe")

    def test(self):
        pass
    