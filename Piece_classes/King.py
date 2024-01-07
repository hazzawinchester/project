from Piece_classes import pieces as parent
from tkinter import messagebox
import numpy as np
from gmpy2 import xmpz
import math

class King(parent.Piece):
    def __init__(self,master,piece,row,col,piece_type):
        super().__init__(master,piece,row,col,piece_type)
        self.legal_moves = xmpz(0)
        if piece.isupper():
            self.master.white_king = self
            self.enemy = self.master.black_positions
            self.friend = self.master.white_positions
        else:
            self.master.black_king = self
            self.enemy = self.master.white_positions
            self.friend = self.master.black_positions

    def destroy(self):
        super().destroy()
        #if self.game_over == False:
        #    messagebox.showinfo(title="Winner!", message="black has won" if self.colour == "w" else "white has won", parent=self.master.master)
        #    self.game_over = True

    def update_legal_moves(self): # not good enough
        #self.ghost_moves = xmpz(460039)
        self.ghost_moves = xmpz(0)
        self.legal_moves = xmpz(0)
        square = int(math.log2(self.pos))
        row,col = square//8,square%8
        up,down,left,right = row-1,row+1,col-1,col+1
        if row>0:
            if self.master.board[up,col].colour != self.colour:
                self.ghost_moves[up*8+col] =1
            if col >0 and  self.master.board[up,left].colour != self.colour:
                self.ghost_moves[up*8+left] =1
            if col <7 and  self.master.board[up,right].colour != self.colour:
                self.ghost_moves[up*8+right] =1
        if row <7:
            if self.master.board[down,col].colour != self.colour:
                self.ghost_moves[down*8+col] =1
            if col >0 and self.master.board[down,left].colour != self.colour:
                self.ghost_moves[down*8+left] =1
            if col <7 and self.master.board[down,right].colour != self.colour:
                self.ghost_moves[down*8+right] =1
        if col >0 and self.master.board[row,left].colour != self.colour:
            self.ghost_moves[row*8+left] =1
        if col <7 and self.master.board[row,right].colour != self.colour:
            self.ghost_moves[row*8+right] =1
            
                
        if self.colour == "w":
            self.legal_moves = self.ghost_moves & ( self.master.black_can_take ^ ((2**64)-1)) # ~ doesnt work as it also flips the sign bit
        else:
            self.legal_moves = self.ghost_moves & ( self.master.white_can_take ^ ((2**64)-1)) # creates a mask of all the places white cant take
        