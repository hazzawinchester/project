import tkinter as tk
from PIL import ImageTk, Image
import numpy as np

pieces_revesed = {'♟': 'p', '♞': 'n', '♝': 'b', '♜': 'r', '♛': 'q', '♚': 'k', '♙': 'P', '♘': 'N', '♗': 'B', '♖': 'R', '♕': 'Q', '♔': 'K'}
file_type = {"classic":"png","periodic":"png"}
values = {"p":100,"n":305,"b":333,"r":563,"q":950,"k":0,'':0}


#https://en.wikipedia.org/wiki/Chess_piece_relative_value#:~:text=The%20best%20known%20system%20assigns,piece%20is%20very%20position%20dependent.

#https://thenounproject.com FOR ICONS 

# piece parent class to all pieces, contains no functionality as each piece is unique 
class Piece(tk.Label):
    def __init__(self,master,piece,row,col,piece_type):
        # '' is used to hold an empty sqaure
        if piece != '':
            #checks if the pieces is white (.isupper() will be True)
            if piece.isupper():
                # fetches the white image corelating to the piece
                self.img = Image.open(f"Pieces/{piece_type}/{piece_type}w{piece.lower()}.{file_type[piece_type]}")
                self.colour ="w"
            else: 
                #fetches the black image corelating to the piece
                self.img = Image.open(f"Pieces/{piece_type}/{piece_type}b{piece}.{file_type[piece_type]}")
                self.colour = "b"
                
            #sets the image to a standard size and applys it to the object    
            self.img = self.img.resize((90, 90))
            self.img = ImageTk.PhotoImage(self.img)
            super().__init__(master,borderwidth=0,image=self.img,bg="gray")
        else:
            #used for empty squares so operations can be generalised to be performed on tk.lable objects
            super().__init__(master,borderwidth=0,bg="white" if (row+col)%2==0 else "gray")
            self.colour = None

        # piece attributes
        self.master=master
        self.pos = [row,col]
        self.ascii = piece
        self.value = values[piece.lower() if piece != '' else '']

    def __str__(self):
        return self.ascii
    
    def update_moves(self,move):
        raise NotImplementedError


class Knight(Piece):
    def __init__(self,master,piece,row,col,piece_type):
        super().__init__(master,piece,row,col,piece_type)
        self.moves = np.zeros((8,8),dtype=int)
        self.master = master

    def update_moves(self,move):
        print(self.master.ascii_board)
 