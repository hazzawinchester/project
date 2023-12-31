import tkinter as tk
 
class Home_page(tk.Frame):
    def __init__(self,master):
        super().__init__(master,bg="#4b4b4b") 
        self.grid_rowconfigure(0, weight = 1)
        self.grid_rowconfigure(1, weight = 15)
        self.grid_columnconfigure(0, weight = 1)

        header = tk.Label(self, text = "WELCOME TO CHESS GAME :^)", font = ("arial",10),bg="#5b5b5b",borderwidth=0)
        header.grid(row=0,column=0,sticky="nesw")