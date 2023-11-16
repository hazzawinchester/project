import tkinter as tk
from tkinter import messagebox
import numpy as np  
import board


def create_board(layout="rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBKQBNR",piece_type="classic"):
    chessboard = board.chessboard(window,layout,piece_type)
    chessboard.place(relx=0.5,rely=0.5, anchor="center")

window = tk.Tk()
window.title("Chess")
window.geometry("800x800")
#window.wm_attributes("-transparentcolor","black")



create_board(piece_type="periodic")

window.mainloop()
