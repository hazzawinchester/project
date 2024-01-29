import tkinter as tk
from tkinter import ttk


class Settings_page(tk.Frame):
    def __init__(self,master):
        super().__init__(master,bg="#4b4b4b")
        self.grid_rowconfigure(0, weight = 1)
        self.grid_rowconfigure(1, weight = 15)
        self.grid_columnconfigure(0, weight = 1)

        header = tk.Label(self, text = "Settings", font = ("arial",10),bg="gray",borderwidth=0)
        header.grid(row=0,column=0,sticky="nesw") 
        
        frame = tk.Frame(self, bg ="#4b4b4b")
        frame.grid(row=1,column=0,sticky="nesw")
        
        button_frame = tk.Frame(self, bg ="#4b4b4b")
        button_frame.grid(row=2, column = 0)
        
        save = tk.Button(button_frame, text = "SAVE",font = ("arial",15),bg="gray",borderwidth=0, command = self.save_settings)
        save.pack(side="left")
        reset = tk.Button(button_frame, text = "RESET",font = ("arial",10),bg="gray",borderwidth=0, command = self.reset_settings)
        reset.pack(side="left")
        
        CheckVar1 = tk.IntVar()
        activate_bot = tk.Checkbutton(frame, bg = "#4b4b4b", text = "Play against bot", variable = CheckVar1, onvalue = 1, offvalue = 0).pack()
        
        
        items = ("ascii","periodic","hidden","secret","classic")
        # datatype of menu text 
        self.clicked = tk.StringVar() 
        self.clicked.set( "ascii" )
        
        self.piece_types = tk.OptionMenu(frame,self.clicked, *items)
        self.piece_types.pack()
        
        self.white_colour = tk.Text(frame,height = 1, width = 50)
        self.black_colour = tk.Text(frame,height = 1, width = 50)
        self.white_colour.insert(tk.END, "#e2bd8d")
        self.black_colour.insert(tk.END, "#300659")
        self.white_colour.pack()
        self.black_colour.pack()



    def save_settings(self):
        board = self.master.frames["Play"]
        board.piece_type = self.clicked.get()
        board.colour_scheme = [self.white_colour.get(1.0, "end-1c"),self.black_colour.get(1.0, "end-1c")]

    def reset_settings(self):
        self.white_colour.delete(1.0,"end")
        self.white_colour.insert(tk.END, "#e2bd8d")
        self.black_colour.delete(1.0,"end")
        self.black_colour.insert(tk.END, "#300659")
        self.clicked.set( "ascii" )
