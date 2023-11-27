import tkinter as tk
import board

import time


# runner that collects all GUI elements to assembel them into the software
def create_board(layout="rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR",piece_type="classic"):
    global chessboard
    # create chessboard instance
    chessboard = board.chessboard(window,layout,piece_type)

    #centers chesboard in the root window
    chessboard.place(relx=0.5,rely=0.5, anchor="center")

#creation of a root window named "chess" with dimensions 800*800 .
s= time.time()

window = tk.Tk()
window.title("Chess")
window.geometry("800x800")

create_board(piece_type="periodic") # 0.3 per iteration

print(time.time()-s)

window.mainloop()



