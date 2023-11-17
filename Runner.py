import tkinter as tk
from tkinter import messagebox
import numpy as np  
import board
import pieces as p


# runner that collects all GUI elements to assembel them into the software


def create_board(layout="rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBKQBNR",piece_type="classic"):
    global chessboard
    # create chessboard instance
    chessboard = board.chessboard(window,layout,piece_type)

    #centers chesboard in the root window
    chessboard.place(relx=0.5,rely=0.5, anchor="center")

#creation of a root window named "chess" with dimensions 800*800 pixels
window = tk.Tk()
window.title("Chess")
window.geometry("800x800")

create_board(piece_type="periodic")

# Loop to run the window with all of its widgets
window.mainloop()



