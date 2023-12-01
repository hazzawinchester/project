import tkinter as tk
import board

import time


# runner that collects all GUI elements to assembel them into the software
def create_board(layout="rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1", piece_type="classic", game_type="p", colour_scheme=["#e2bd8d","#421e00"]):#"#e2bd8d","#421e00"
    global chessboard
    chessboard = board.chessboard(window,layout,piece_type,game_type,colour_scheme)

    #centers chesboard in the root window
    chessboard.place(relx=0.5,rely=0.5, anchor="center")


window = tk.Tk()
window.title("Chess")
window.geometry("800x800")
window.configure(bg="#2b2b2b")

create_board(piece_type="periodic") # 0.04 per iteration

window.mainloop()



