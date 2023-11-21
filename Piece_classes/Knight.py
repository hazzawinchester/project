from Piece_classes import pieces as parent
import numpy as np
class Knight(parent.Piece):
    def __init__(self,master,piece,row,col,piece_type):
        super().__init__(master,piece,row,col,piece_type)

    def update_legal_moves(self):
        self.legal_moves = [[100,100]]
#        self.legal_moves_array = np.zeros((8,8),dtype=str)
        row,col = self.pos[0],self.pos[1] 

        if col>=2 and row >=1 and self.master.board[row-1,col-2].colour != self.colour:
            self.legal_moves = np.append(self.legal_moves,[[(row-1),(col-2)]], axis=0)
#            self.legal_moves_array[row-1,col-2] = self.master.ascii_board[row-1,col-2] if self.master.board[row-1,col-2].colour != None else "x"
        if col>=2 and row <=6 and self.master.board[row+1,col-2].colour != self.colour:
            self.legal_moves = np.append(self.legal_moves,[[(row+1),(col-2)]], axis=0)
#            self.legal_moves_array[row+1,col-2] = self.master.ascii_board[row+1,col-2] if self.master.board[row+1,col-2].colour != None else "x"    
        
        if col>=1 and row >=2 and self.master.board[row-2,col-1].colour != self.colour:
            self.legal_moves = np.append(self.legal_moves,[[(row-2),(col-1)]], axis=0)
#            self.legal_moves_array[row-2,col-1] = self.master.ascii_board[row-2,col-1] if self.master.board[row-2,col-1].colour != None else "x"
        if col>=1 and row <=5 and self.master.board[row+2,col-1].colour != self.colour:
            self.legal_moves = np.append(self.legal_moves,[[(row+2),(col-1)]], axis=0)
#            self.legal_moves_array[row+2,col-1] = self.master.ascii_board[row+2,col-1] if self.master.board[row+2,col-1].colour != None else "x"


        if col<=5 and row >=1 and self.master.board[row-1,col+2].colour != self.colour:
            self.legal_moves = np.append(self.legal_moves,[[(row-1),(col+2)]], axis=0)
#            self.legal_moves_array[row-1,col+2] = self.master.ascii_board[row-1,col+2] if self.master.board[row-1,col+2].colour != None else "x"
        if col<=5 and row <=6 and self.master.board[row+1,col+2].colour != self.colour:
            self.legal_moves = np.append(self.legal_moves,[[(row+1),(col+2)]], axis=0)
#           self.legal_moves_array[row+1,col+2] = self.master.ascii_board[row+1,col+2] if self.master.board[row+1,col+2].colour != None else "x"
        
        if col <=6 and row >=2 and self.master.board[row-2,col+1].colour != self.colour:
            self.legal_moves = np.append(self.legal_moves,[[(row-2),(col+1)]], axis=0)
#            self.legal_moves_array[row-2,col+1] = self.master.ascii_board[row-2,col+1] if self.master.board[row-2,col+1].colour != None else "x"
        if col <=6 and row <=5 and self.master.board[row+2,col+1].colour != self.colour:
            self.legal_moves = np.append(self.legal_moves,[[(row+2),(col+1)]], axis=0)
#            self.legal_moves_array[row+2,col+1] = self.master.ascii_board[row+2,col+1] if self.master.board[row+2,col+1].colour != None else "x"