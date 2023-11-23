from Piece_classes import pieces as parent
import numpy as np

class Pawn(parent.Piece):
    def __init__(self,master,piece,row,col,piece_type):
        super().__init__(master,piece,row,col,piece_type)
        self.has_moved = False

    def update_legal_moves(self):
        self.legal_moves = [[100,100]]
        self.legal_moves_array = np.zeros((8,8),dtype=str)
        row,col = self.pos[0],self.pos[1]

        up1 = row- 1
        up2 = row- 2
        down1 = row+ 1
        down2 = row+ 2
        left1 = col- 1
        right1= col+ 1
        
        
        if self.colour == "w":
            if row>=1 and self.master.board[up1,col].colour == None:
                self.legal_moves = np.append(self.legal_moves,[[(up1),col]], axis=0)        
                if self.master.board[up2,col].colour == None and not self.has_moved:
                    self.legal_moves = np.append(self.legal_moves,[[(up2),col]], axis=0)

            #taking 
            if row>=1 and col>=1 and self.master.board[up1,left1].colour != None and self.master.board[up1,left1].colour != self.colour:
                self.legal_moves = np.append(self.legal_moves,[[(up1),(left1)]], axis=0)
            if row>=1 and col<=6 and self.master.board[up1,right1].colour != None and self.master.board[up1,right1].colour != self.colour:
                self.legal_moves = np.append(self.legal_moves,[[(up1),(right1)]], axis=0)
        else:
            if row<=6 and self.master.board[down1,col].colour == None:
                self.legal_moves = np.append(self.legal_moves,[[(down1),col]], axis=0)        
                if self.master.board[down2,col].colour == None and not self.has_moved:
                    self.legal_moves = np.append(self.legal_moves,[[(down2),col]], axis=0)

            #taking 
            if row<=6 and col>=1 and self.master.board[down1,left1].colour != None and self.master.board[down1,left1].colour != self.colour:
                self.legal_moves = np.append(self.legal_moves,[[(down1),(left1)]], axis=0)
            if row<=6 and col<=6 and self.master.board[down1,right1].colour != None and self.master.board[down1,right1].colour != self.colour:
                self.legal_moves = np.append(self.legal_moves,[[(down1),(right1)]], axis=0)

        