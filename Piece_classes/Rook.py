from Piece_classes import pieces as parent
import numpy as np
import time
from gmpy2 import xmpz
import math

class Rook(parent.Piece):
    def __init__(self,master,piece,row,col,piece_type):
        super().__init__(master,piece,row,col,piece_type)


    def update_legal_moves(self):  # 2.6*10^-6 per move max
        self.legal_moves = xmpz(0)
        self.ghost_moves = xmpz(0)
        square = int(math.log2(self.pos))
        row,col = square//8,square%8
        left,right,up,down,a = False,False,False,False,1
        while left==False or right==False or up==False or down==False:
            if left == False:
                if col-a >=0:
                    left = self.check_square((row<<3)+(col-a),left)
                else:
                    left = True

            if right == False:
                if col+a <=7:
                    right = self.check_square((row<<3)+(col+a),right)
                else:
                    right = True

            if up == False:
                if row-a >=0:
                    up = self.check_square(((row-a)<<3)+col,up)
                else:
                    up = True

            if down == False:
                if row+a <=7:
                    down = self.check_square(((row+a)<<3)+col,down)
                else:
                    down = True
            a+=1        
"""        
    def update_ghost_moves(self):
        self.ghost_moves = [[100,100]]
        row,col = self.pos
        self.ghost_moves=  np.append(self.ghost_moves,[(a,col) for a in range(8)], axis=0)
        self.ghost_moves=  np.append(self.ghost_moves,[(row,a) for a in range(8)], axis=0)
        """


