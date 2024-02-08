import tkinter as tk
from tkinter import ttk
from Piece_classes import Pawn
from Chess_board import Move_handler

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
        reset = tk.Button(button_frame, text = "RESET",font = ("arial",15),bg="gray",borderwidth=0, command = self.reset_settings)
        reset.pack(side="left")
        
        CheckVar1 = tk.IntVar()
        activate_bot = tk.Checkbutton(frame, bg = "#4b4b4b", text = "Play against bot", variable = CheckVar1, onvalue = 1, offvalue = 0).pack()
        
        
        items = ("ascii","periodic","hidden","secret","classic")
        # datatype of menu text 
        self.clicked = tk.StringVar() 
        self.clicked.set( "ascii" )
        
        self.piece_types = tk.OptionMenu(frame,self.clicked, *items)
        self.piece_types.pack()
        
        #self.colour_scheme = {"white":"#e2bd8d","black":"#5e2496"}
        
        self.white_colour = tk.Text(frame,height = 1, width = 50)
        self.black_colour = tk.Text(frame,height = 1, width = 50)
        self.white_colour.insert(tk.END, "#e2bd8d")
        self.black_colour.insert(tk.END, "#5e2496")
        self.white_colour.pack()
        self.black_colour.pack()
        
        self.example_board = Temp_board(frame,{"white":"#5e2496","black":"#e2bd8d"})
        self.example_board.pack(side="right")
        
        for row in range(3):
            for col in range(3):
                tk.Frame(self.example_board, bg=self.white_colour.get(1.0, "end-1c")  if (row+col)%2==1 else self.black_colour.get(1.0, "end-1c") ,width=100, height=100, borderwidth=4).grid(row=row,column=col)
        
        self.example_pawn = Example_pawn(self.example_board,self.clicked.get())
        self.example_board.move_handler.add_dragable(self.example_pawn)
        self.example_pawn.update_legal_moves()
        self.example_pawn.grid(row=2,column=1)



    def save_settings(self):
        try:
            board = self.master.frames["Play"]
            board.piece_type = self.clicked.get()
            board.colour_scheme = [self.white_colour.get(1.0, "end-1c"),self.black_colour.get(1.0, "end-1c")]
            self.example_board.piece_type = self.clicked.get()

            
            squares= 0
            self.example_pawn.destroy()
            self.example_pawn = Example_pawn(self.example_board,self.clicked.get())
            self.example_board.move_handler.add_dragable(self.example_pawn)
            self.example_pawn.update_legal_moves()
            self.example_pawn.grid(row=2,column=1)
            
            for i in self.example_board.grid_slaves():
                row,col = squares %3,squares//3
                i.configure(bg=self.white_colour.get(1.0, "end-1c")  if (row+col)%2==0 else self.black_colour.get(1.0, "end-1c") )
                squares +=1

            tk.messagebox.showinfo(title="SAVED", message="Settings Saved!")
        except:
            tk.messagebox.showinfo(title="ERROR", message="invalid settings input")
        
    def reset_settings(self):
        self.white_colour.delete(1.0,"end")
        self.white_colour.insert(tk.END, "#e2bd8d")
        self.black_colour.delete(1.0,"end")
        self.black_colour.insert(tk.END, "#5e2496")
        self.example_board.colour_scheme = {"white":"#5e2496","black":"#e2bd8d"}
        self.example_board.piece_type = "ascii"
        

        self.clicked.set( "ascii" )


class Temp_board(tk.Frame):
    def __init__(self,frame,colours):
        super().__init__(frame, height = 240, width = 240)
        self.colour_scheme = colours
        self.black_positions = 0
        self.white_positions = 0
        self.white_pieces = []
        self.black_pieces = []
        self.piece_list = []
        self.border_width = 0
        self.active_colour = "w"
        self.en_passant = 0
        self.piece_type = "ascii"
        self.move_handler = Move_handler.Move_handler(self)
        self.move_handler.on_drop = self.drop
        self.bpawn = 1
        self.wpawn = 9
        
    def drop(self,move):
        pass
        
class Example_pawn(Pawn.Pawn):
    def __init__(self,master,type):
        super().__init__(master,9,2,1,type)
    