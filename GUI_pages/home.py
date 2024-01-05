import tkinter as tk
from tkinter import ttk
 
class Home_page(tk.Frame):
    def __init__(self,master):
        self.master = master
        super().__init__(master,bg="#4b4b4b") 

        header = tk.Label(self, text = "WELCOME TO CHESS GAME :^)", font = ("arial",20),bg="#5b5b5b",borderwidth=0)
        header.grid(row=0,column=0,sticky="nesw",columnspan=2)
        
        frame = tk.Frame(self, bg ="#4b4b4b")
        frame.grid(row=1,column=0,sticky="nesw")
        tk.Frame(frame, bg = "#4b4b4b", height = 50).pack(anchor="center")
        tk.Button(frame,bg = "Blue",fg ="White",width=20, height= 2, font= ("arial",20),text = "play", command = lambda : (self.master.show_frame("Play"), self.master.frames["Play"].create_board(self.master.frames["Play"],piece_type="ascii"),self.master.lastpage.append("Home"))).pack(anchor="center",pady=50)
        tk.Button(frame,bg = "Blue",fg ="White",width=15 ,height= 2, font= ("arial",20),text = "variants", command = lambda : (self.master.show_frame("Variants"),self.master.lastpage.append("Home"))).pack(anchor="center",pady=0)
        
        self.grid_rowconfigure(0, weight = 1)
        self.grid_rowconfigure(1, weight = 8)
        self.grid_rowconfigure(2, weight = 8)
        self.grid_columnconfigure(0, weight = 1)
        self.grid_columnconfigure(1, weight = 1)
        
        
        