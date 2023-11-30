from Piece_classes import pieces as parent
from numpy import append


class Pawn(parent.Piece):
    def __init__(self,master,piece,row,col,piece_type):
        super().__init__(master,piece,row,col,piece_type)
        self.has_moved = False

    def update_legal_moves(self): 
        self.legal_moves = [[100,100]]
        row,col = self.pos[0],self.pos[1]        
        
        if self.colour == "w":
            self.pawn_moves(row,row- 1,row- 2,col,self.master.board)
        else:
            self.pawn_moves(row,row+ 1,row+ 2,col,self.master.board)

            
    def pawn_moves(self,row,row1,row2,col,board):
        left1 = col- 1
        right1= col+ 1

        if row>=1 and board[row1,col].colour == None:
            self.legal_moves = append(self.legal_moves,[[(row1),col]], axis=0)        
            if board[row2,col].colour == None and not self.has_moved:
                self.legal_moves = append(self.legal_moves,[[(row2),col]], axis=0)

        #taking 
        if row>=1 and col>=1 and board[row1,left1].colour != None and board[row1,left1].colour != self.colour:
            self.legal_moves = append(self.legal_moves,[[(row1),(left1)]], axis=0)
        if row>=1 and col<=6 and board[row1,right1].colour != None and board[row1,right1].colour != self.colour:
            self.legal_moves = append(self.legal_moves,[[(row1),(right1)]], axis=0)

