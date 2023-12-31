import tkinter as tk
from tkinter import ttk
import board

class Chess_game(tk.Frame):
    def __init__(self,master,piece_type):
        super().__init__(master,bg="#4b4b4b")
        self.piece_type = piece_type
        
        ttk.Button(self,width=10, text = "Play", command = lambda : self.create_board(self,piece_type=self.piece_type)).pack()
        ttk.Button(self,width=10, text = "Resign", command = self.delete_board).pack()
        
    
    def create_board(self,master,FEN="rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1",stack=[], piece_type="classic", game_type="p", colour_scheme=["#e2bd8d","#421e00"]):#"#e2bd8d","#421e00"
        self.chessboard = board.chessboard(master,FEN,stack,piece_type,game_type,colour_scheme)

        #centers chesboard in the root window
        self.chessboard.place(relx=0.5,rely=0.5, anchor="center")
    
    def delete_board(self):
        self.last_game = self.chessboard.destroy()
        del self.chessboard # to prevent wasted memory
        