from Piece_classes import pieces as parent
from tkinter import messagebox
import numpy as np
from gmpy2 import xmpz
import math

class King(parent.Piece):
    def __init__(self,master,piece,row,col,piece_type):
        super().__init__(master,piece,row,col,piece_type)
        self.legal_moves = xmpz(0)
        if self.colour: # passed by reference so it stays up to date
            self.master.white_king = self
            self.friend = self.master.white_positions
            self.enemy_can_take = self.master.black_can_take
        else:
            self.master.black_king = self
            self.friend = self.master.black_positions
            self.enemy_can_take = self.master.white_can_take

    def destroy(self):
        super().destroy()
        #if self.game_over == False:
        #    messagebox.showinfo(title="Winner!", message="black has won" if self.colour == "w" else "white has won", parent=self.master.master)
        #    self.game_over = True

        
    def update_legal_moves(self):

        pos = int(math.log2(self.pos))
        top =  ((896 << (pos % 8)) & 65280) >> 8
        bottom = ((896 << (pos % 8)) & 65280) <<8
        current = ((640 << (pos % 8)) & 65280) 

        if pos >7 and pos < 56:
            self.ghost_moves = ((current) << 8*((pos-8) //8)) | ((top) << 8*((pos-8) //8)) | ((bottom) << 8*((pos-8) //8))
        elif pos <= 7:
            self.ghost_moves = ((current) >> 8) |  ((bottom) >> 8)
        else:
            self.ghost_moves = ((current) << 8*((pos-8) //8)) | ((top) << 8*((pos-8) //8))
        
        self.legal_moves = self.ghost_moves & ~(self.friend | self.enemy_can_take)
        
        #castling

          
        if not self.has_moved:
            row = (126 << (8*((pos) //8)))
            left  = (14 << (8*((pos) //8)))
            right = (96 << (8*((pos) //8)))
            if self.colour:
                if self.master.available_castle[3] and not (right & (self.master.white_positions | self.master.black_positions | self.enemy_can_take)):
                    self.legal_moves |= 4611686018427387904
                
                if self.master.available_castle[2] and not (left & (self.master.white_positions | self.master.black_positions | self.enemy_can_take)):
                    self.legal_moves |= 288230376151711744
            else:
                if self.master.available_castle[1] and not (right & (self.master.white_positions | self.master.black_positions | self.enemy_can_take)):
                    self.legal_moves |= 64
                
                if self.master.available_castle[0] and not (left & (self.master.white_positions | self.master.black_positions | self.enemy_can_take)):
                    self.legal_moves |= 4
                    
            
            
            
            
            
            if not (row & ((self.master.white_positions | self.master.black_positions | self.enemy_can_take) ^ self.pos)):
                self.legal_moves |= (self.pos << 2) | (self.pos >> 2)
            
    
        
    # def update_legal_moves(self): # not good enough
    #     #self.ghost_moves = xmpz(460039)
    #     self.ghost_moves = xmpz(0)
    #     self.legal_moves = xmpz(0)
    #     square = int(math.log2(self.pos))
    #     row,col = square//8,square%8
    #     up,down,left,right = row-1,row+1,col-1,col+1
    #     if row>0:
    #         if self.master.board[up,col].colour != self.colour:
    #             self.ghost_moves[up*8+col] =1
    #         if col >0 and  self.master.board[up,left].colour != self.colour:
    #             self.ghost_moves[up*8+left] =1
    #         if col <7 and  self.master.board[up,right].colour != self.colour:
    #             self.ghost_moves[up*8+right] =1
    #     if row <7:
    #         if self.master.board[down,col].colour != self.colour:
    #             self.ghost_moves[down*8+col] =1
    #         if col >0 and self.master.board[down,left].colour != self.colour:
    #             self.ghost_moves[down*8+left] =1
    #         if col <7 and self.master.board[down,right].colour != self.colour:
    #             self.ghost_moves[down*8+right] =1
    #     if col >0 and self.master.board[row,left].colour != self.colour:
    #         self.ghost_moves[row*8+left] =1
    #     if col <7 and self.master.board[row,right].colour != self.colour:
    #         self.ghost_moves[row*8+right] =1
            
                
    #     if self.colour == "w":
    #         self.legal_moves = self.ghost_moves & ( self.master.black_can_take ^ ((2**64)-1)) # ~ doesnt work as it also flips the sign bit
    #     else:
    #         self.legal_moves = self.ghost_moves & ( self.master.white_can_take ^ ((2**64)-1)) # creates a mask of all the places white cant take
            
    #     # castling
    #     row = xmpz(511)
    #     print(bin(row))