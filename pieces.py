import tkinter as tk
from PIL import ImageTk, Image

pieces_revesed = {'♟': 'p', '♞': 'n', '♝': 'b', '♜': 'r', '♛': 'q', '♚': 'k', '♙': 'P', '♘': 'N', '♗': 'B', '♖': 'R', '♕': 'Q', '♔': 'K'}
file_type = {"classic":"png","periodic":"png"}

#
#https://thenounproject.com FOR ICONS 
#

class Piece(tk.Label):
    def __init__(self,master,piece,row,col,piece_type):
        if piece != '':
            if pieces_revesed[piece].isupper():
                self.img = Image.open(f"Pieces/{piece_type}/{piece_type}w{pieces_revesed[piece].lower()}.{file_type[piece_type]}")
            else: 
                self.img = Image.open(f"Pieces/{piece_type}/{piece_type}b{pieces_revesed[piece]}.{file_type[piece_type]}")
                
            self.img = self.img.resize((90, 90))
            self.img = ImageTk.PhotoImage(self.img)
            super().__init__(master,borderwidth=0,image=self.img,bg="pink")

            self.colour = "w" if pieces_revesed[piece].isupper() else "b"
        else:
            super().__init__(master,borderwidth=0,bg="white" if (row+col)%2==0 else "gray")

            self.colour = None

        self.master=master
 