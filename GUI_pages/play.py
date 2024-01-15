import tkinter as tk
from tkinter import ttk
from Chess_board import board

class Chess_game(tk.Frame):
    def __init__(self,master,piece_type,):
        super().__init__(master,bg="#4b4b4b")
        self.piece_type = piece_type
        self.chessboard = None
        self.master = master
        ttk.Button(self,width=10, text = "Play", command = lambda : self.create_board(self,piece_type=self.piece_type)).pack()
        ttk.Button(self,width=10, text = "Resign", command = self.delete_board).pack()
        ttk.Button(self,width=10, text = "randomise", command = self.random_move).pack()
        self.update_board = tk.Text(self,height = 1, width = 50, )
        self.update_button = tk.Button(self,text="import board using FEN", command=self.import_board)
        self.update_board.place(relx=0.5,rely=0.93, anchor="s")
        self.update_button.place(relx=0.5,rely=1, anchor="s")
        
    
    def create_board(self,master,FEN="rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1",stack=[], piece_type="ascii", game_type="p", colour_scheme=["#e2bd8d","#300659"]):#"#e2bd8d","#421e00"  libs #300659
        if self.chessboard != None:
            self.chessboard.destroy()
        
        self.chessboard = board.chessboard(master,FEN,stack,piece_type,game_type,colour_scheme)

        #centers chesboard in the root window
        self.chessboard.place(relx=0.5,rely=0.5, anchor="center")
    
    def delete_board(self):
        self.last_game = self.chessboard.destroy()
        #del self.chessboard # to prevent wasted memory
        self.chessboard == None
        
    def import_board(self):
        inp = self.update_board.get(1.0, "end-1c") 
        self.create_board(self.master,FEN=str(inp),piece_type=self.piece_type)
  
    def random_move(self):
        self.chessboard.make_random_moves(10)