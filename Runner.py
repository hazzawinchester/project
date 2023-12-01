import tkinter as tk
import board

import time


# runner that collects all GUI elements to assembel them into the software
def create_board(layout="rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1", piece_type="classic", game_type="2p", colour_scheme=["pink","purple"]):
    global chessboard
    chessboard = board.chessboard(window,layout,piece_type,game_type,colour_scheme)

    #centers chesboard in the root window
    chessboard.place(relx=0.5,rely=0.5, anchor="center")

#s= time.time()

window = tk.Tk()
window.title("Chess")
window.geometry("800x800")
window.configure(bg="#2b2b2b")

create_board(piece_type="periodic") # 0.3 per iteration

#print(time.time()-s)

window.mainloop()



