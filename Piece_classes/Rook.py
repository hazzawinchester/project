from Piece_classes import pieces as parent
import numpy as np
import time


class Rook(parent.Piece):
    def __init__(self,master,piece,row,col,piece_type):
        super().__init__(master,piece,row,col,piece_type)


    def update_legal_moves(self):  # 4*10^-9 per move max
        self.legal_moves = [[100,100]]
        row,col = self.pos[0],self.pos[1]
        left,right,up,down,a = False,False,False,False,1
        while left==False or right==False or up==False or down==False:
            if left == False:
                if col-a >=0:
                    left = self.check_square(row,(col-a),left)
                else:
                    left = True

            if right == False:
                if col+a <=7:
                    right = self.check_square(row,(col+a),right)
                else:
                    right = True

            if up == False:
                if row-a >=0:
                    up = self.check_square((row-a),col,up)
                else:
                    up = True

            if down == False:
                if row+a <=7:
                    down = self.check_square((row+a),col,down)
                else:
                    down = True
            a+=1
        
        
    def update_ghost_moves(self):
        pass
    
        # self.all_possible_moves = np.zeros((8,8),dtype=str)
        # row,col = self.pos[0],self.pos[1]
        # left,right,up,down,a = False,False,False,False,1
        
        # while left==False or right==False or up==False or down==False:
        #     pass

