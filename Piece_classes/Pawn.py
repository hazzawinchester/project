from Piece_classes import pieces as parent
from gmpy2 import xmpz
import time



class Pawn(parent.Piece):
    def __init__(self,master,piece,row,col,piece_type):
        super().__init__(master,piece,row,col,piece_type)
        self.has_moved = 0

    def update_legal_moves(self): # 5*10-6 per move generated
            self.legal_moves = xmpz(0)
            self.ghost_moves = xmpz(0)
            row,col = self.pos[0],self.pos[1]   
            board = self.master.board

            if self.colour == "w":
                self.check_forward(board,row-1,row-2,col)
                self.check_take(board,row-1,col)
            else:
                self.check_forward(board,row+1,row+2,col)
                self.check_take(board,row+1,col)



    def check_forward(self,board,row1,row2,col):
        if board[row1,col].colour == None:
            blocked = self.check_square(row1,col)
            if (not self.has_moved) and (not blocked) and (row2 >=0 and row2<=7): #and (board[row2,col].colour == None):
                self.check_square(row2,col)
            else:
                self.ghost_moves[row2*8+col] =1
        else:
            self.ghost_moves[row1*8+col] =1

    def check_take(self,board,row,col):
        left,right = col-1,col+1
        if col>=1:
            pos = xmpz(0)
            pos[row*8+left] =1 
            if not board[row,left].colour in (None,self.colour) or (pos & self.master.en_passent):
                self.legal_moves[row*8+left] =1
            self.ghost_moves[row*8+left] =1
        if col <=6:
            pos = xmpz(0)
            pos[row*8+right] =1 
            if not board[row,right].colour in (None,self.colour) or (pos & self.master.en_passent):
                self.legal_moves[row*8+right] =1
            self.ghost_moves[row*8+right] =1




"""             if row1<=7 and col>=1 and not board[row1,left].colour in (None,self.colour):
                self.legal_moves = append(self.legal_moves,[[row1,left]], axis=0)
                self.ghost_moves = append(self.ghost_moves,[[row1,left]], axis=0)
            if row1<=7 and col<=6:
                if not board[row1,right].colour in (None,self.colour):
                    self.legal_moves = append(self.legal_moves,[[row1,right]], axis=0)
                self.ghost_moves = append(self.ghost_moves,[[row1,left]], axis=0)
                self.ghost_moves = append(self.ghost_moves,[[row1,right]], axis=0)

    def pawn_moves(self,row,row1,row2,col,board):
        left1 = col- 1
        right1= col+ 1

        if row1>=0 and row1<=7 and board[row1,col].colour == None:
            self.check_square(row1,col)       
            if board[row2,col].colour == None and not self.has_moved:
                self.check_square(row1,col)

        #taking 
        if row>=1 and col>=1 and board[row1,left1].colour != None and board[row1,left1].colour != self.colour:
            self.legal_moves = append(self.legal_moves,[[(row1),(left1)]], axis=0)
        if row>=1 and col<=6 and board[row1,right1].colour != None and board[row1,right1].colour != self.colour:
            self.legal_moves = append(self.legal_moves,[[(row1),(right1)]], axis=0)

 """