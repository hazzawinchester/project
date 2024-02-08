import tkinter as tk
from tkinter import ttk
from Chess_board import board

class Chess_game(tk.Frame):
    def __init__(self,master,piece_type):
        super().__init__(master,bg="#4b4b4b")
        self.chessboard = None
        self.master = master
        
        self.piece_type = piece_type
        self.colour_scheme = ["#e2bd8d","#5e2496"]
        
        ttk.Button(self,width=10, text = "Play", command = self.create_board).pack()
        ttk.Button(self,width=10, text = "Resign", command = self.delete_board).pack()
        
        self.CheckVar1 = tk.BooleanVar()
        tk.Checkbutton(self, bg = "#4b4b4b", text = "Play against bot", variable = self.CheckVar1, onvalue = 1, offvalue = 0, command= self.random_move).pack()
        #ttk.Button(self,width=10, text = "randomise", command = self.random_move).pack()
        self.update_board = tk.Text(self,height = 1, width = 60, )
        self.update_button = tk.Button(self,text="import board using FEN", command=self.import_board)
        self.update_board.place(relx=0.5,rely=0.93, anchor="s")
        self.update_button.place(relx=0.5,rely=1, anchor="s")
        
    
    def create_board(self,FEN="rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1",stack=[], game_type="p"):#"#e2bd8d","#421e00"  libs #300659
        if self.chessboard: 
            self.chessboard.destroy()
        
        self.chessboard = board.chessboard(self,FEN,stack,self.piece_type,game_type,self.colour_scheme)

        #centers chesboard in the root window
        self.chessboard.place(relx=0.5,rely=0.5, anchor="center")
    
    def delete_board(self):
        self.last_game = self.chessboard.destroy()
        #del self.chessboard # to prevent wasted memory
        self.chessboard == None
        
    def import_board(self):
        inp = self.update_board.get(1.0, "end-1c") 
        self.create_board(FEN=str(inp))
  
    def random_move(self):
        while self.CheckVar1:
            self.chessboard.make_random_moves(1)
            