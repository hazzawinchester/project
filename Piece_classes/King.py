from Piece_classes import pieces as parent
from tkinter import messagebox
import numpy as np
from gmpy2 import xmpz

class King(parent.Piece):
    def __init__(self,master,piece,row,col,piece_type):
        super().__init__(master,piece,row,col,piece_type)
        self.legal_moves = np.array([[100,100]])
        if piece.isupper():
            self.master.white_king = self
        else:
            self.master.black_king = self

    def destroy(self):
        super().destroy()
        #if self.game_over == False:
        #    messagebox.showinfo(title="Winner!", message="black has won" if self.colour == "w" else "white has won", parent=self.master.master)
        #    self.game_over = True

    def update_legal_moves(self): # not good enough
        #self.ghost_moves = xmpz(460039)
        self.ghost_moves = xmpz(2**63-1)
        self.legal_moves = xmpz(0)
        row,col = self.pos
        
        if self.colour == "w":
            self.legal_moves = self.ghost_moves & ( self.master.black_can_take ^ ((2**64)-1)) # ~ doesnt work as it also flips the sign bit
        else:
            self.legal_moves = self.ghost_moves & ( self.master.white_can_take ^ ((2**64)-1)) # creates a mask of all the places white cant take
