from Piece_classes import pieces as parent

class Knight(parent.Piece):
    def __init__(self,master,piece,row,col,piece_type):
        super().__init__(master,piece,row,col,piece_type)

    def update_legal_moves(self):
        self.legal_moves = [[100,100]]
        self.ghost_moves = [[100,100]]
        row,col = self.pos[0],self.pos[1] 

        up1 = row-1
        up2 = row-2
        down1 = row+1
        down2 = row+2
        left1 = col-1
        left2 = col-2
        right1 = col+1
        right2 = col+2

        if col >=1:
            if row >=2:
                self.check_square(up2,left1)
            if row <=5:
                self.check_square(down2,left1)
            if col >= 2:
                if row >=1:
                    self.check_square(up1,left2)
                if row <=6:
                    self.check_square(down1,left2)

        if col <= 6:
            if row >=2:
                self.check_square(up2,right1)
            if row <=5:
                self.check_square(down2,right1)
                
            if col <= 5:
                if row >=1:
                    self.check_square(up1,right2)
                if row <=6:
                    self.check_square(down1,right2)





""" 
if col >=1:
            if row >=2 and self.master.board[up2,left1].colour != self.colour:
                self.legal_moves = np.append(self.legal_moves,[[(up2),(left1)]], axis=0)
            if row <=5 and self.master.board[down2,left1].colour != self.colour:
                self.legal_moves = np.append(self.legal_moves,[[(down2),(left1)]], axis=0)

            if col >= 2:
                if row >=1 and self.master.board[up1,left2].colour != self.colour:
                    self.legal_moves = np.append(self.legal_moves,[[(up1),(left2)]], axis=0)
                if row <=6 and self.master.board[down1,left2].colour != self.colour:
                    self.legal_moves = np.append(self.legal_moves,[[(down1),(left2)]], axis=0)
            
        if col <= 6:
            if row >=2 and self.master.board[up2,right1].colour != self.colour:
                self.legal_moves = np.append(self.legal_moves,[[(up2),(right1)]], axis=0)
            if row <=5 and self.master.board[down2,right1].colour != self.colour:
                self.legal_moves = np.append(self.legal_moves,[[(down2),(right1)]], axis=0)
                
            if col <= 5:
                if row >=1 and self.master.board[up1,right2].colour != self.colour:
                    self.legal_moves = np.append(self.legal_moves,[[(up1),(right2)]], axis=0)
                if row <=6 and self.master.board[down1,right2].colour != self.colour:
                    self.legal_moves = np.append(self.legal_moves,[[(down1),(right2)]], axis=0)
 """

