import tkinter as tk
from tkinter import messagebox
import numpy as np
import board

window = tk.Tk()
window.title("Chess")
window.geometry("800x800")

chessboard = board.chessboard(window,"rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR")
chessboard.place(relx=0.5,rely=0.5, anchor="center")
print(chessboard.board)

window.mainloop()

