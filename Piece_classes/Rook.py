from Piece_classes import pieces as parent
import numpy as np
import time


class Rook(parent.Piece):
    def __init__(self,master,piece,row,col,piece_type):
        super().__init__(master,piece,row,col,piece_type)


    def update_legal_moves(self):  # 1.2*10^-4 per move max
        self.legal_moves = [[100,100]]
#        self.legal_moves_array = np.zeros((8,8),dtype=str)
        row,col = self.pos[0],self.pos[1]
        left,right,up,down,a = False,False,False,False,1

        while left==False or right==False or up==False or down==False:

            if left == False and col-a >= 0 and self.master.board[row,col-a].colour == None:
                self.legal_moves = np.append(self.legal_moves,[[row,(col-a)]], axis=0)
#                self.legal_moves_array[row,col-a] = self.master.ascii_board[row,col-a] if self.master.board[row,col-a].colour != None else "x"
            else:
                if col-a >= 0 and self.master.board[row,col-a].colour != None and self.master.board[row,col-a].colour != self.colour and left != True:
                    self.legal_moves = np.append(self.legal_moves,[[row,(col-a)]], axis=0)
#                    self.legal_moves_array[row,col-a] = self.master.ascii_board[row,col-a]
                left = True

            if right == False and col+a <= 7 and self.master.board[row,col+a].colour == None:
                self.legal_moves = np.append(self.legal_moves,[[row,(col+a)]], axis=0)
#                self.legal_moves_array[row,col+a] = self.master.ascii_board[row,col+a] if self.master.board[row,col+a].colour != None else "x"
            else:
                if col+a <= 7 and self.master.board[row,col+a].colour != None and self.master.board[row,col+a].colour != self.colour and right != True:
                    self.legal_moves = np.append(self.legal_moves,[[row,(col+a)]], axis=0)                  
#                    self.legal_moves_array[row,col+a] = self.master.ascii_board[row,col+a]
                right = True

            if down == False and row-a >= 0 and self.master.board[row-a,col].colour == None:
                self.legal_moves = np.append(self.legal_moves,[[(row-a),col]], axis=0)  
#                self.legal_moves_array[row-a,col] = self.master.ascii_board[row-a,col] if self.master.board[row-a,col].colour != None else "x"
            else:
                if row-a >= 0 and self.master.board[row-a,col].colour != None and self.master.board[row-a,col].colour != self.colour and down != True:
                    self.legal_moves = np.append(self.legal_moves,[[(row-a),col]], axis=0)                 
#                    self.legal_moves_array[row-a,col] = self.master.ascii_board[row-a,col]                
                down = True

            if up == False and row+a <= 7 and self.master.board[row+a,col].colour == None:
                self.legal_moves = np.append(self.legal_moves,[[(row+a),col]], axis=0)
#                self.legal_moves_array[row+a,col] = self.master.ascii_board[row+a,col] if self.master.board[row+a,col].colour != None else "x"
            else:
                if row+a <= 7 and self.master.board[row+a,col].colour != None and self.master.board[row+a,col].colour != self.colour and up != True:
                    self.legal_moves = np.append(self.legal_moves,[[(row+a),col]], axis=0)                  
#                    self.legal_moves_array[row+a,col] = self.master.ascii_board[row+a,col]                
                up = True

            a+=1
        
    def update_possible_moves(self):
        self.all_possible_moves = np.zeros((8,8),dtype=str)
        row,col = self.pos[0],self.pos[1]
        left,right,up,down,a = False,False,False,False,1
        
        while left==False or right==False or up==False or down==False:
            pass

"""
while left==False or right==False or up==False or down==False:

            if left == False and col-a >= 0 and self.master.board[row,col-a].colour == None:
                self.legal_moves = np.append(self.legal_moves,[[row,(col-a)]], axis=0)
                self.legal_moves_array[row,col-a] = self.master.ascii_board[row,col-a] if self.master.board[row,col-a].colour != None else "x"
            else:
                if col-a >= 0 and self.master.board[row,col-a].colour != None and self.master.board[row,col-a].colour != self.colour and left != True:
                    self.legal_moves.append([row,(col-a)])
                    self.legal_moves_array[row,col-a] = self.master.ascii_board[row,col-a]
                left = True

            if right == False and col+a <= 7 and self.master.board[row,col+a].colour == None:
                self.legal_moves.append([row,(col+a)])
                self.legal_moves_array[row,col+a] = self.master.ascii_board[row,col+a] if self.master.board[row,col+a].colour != None else "x"
            else:
                if col+a <= 7 and self.master.board[row,col+a].colour != None and self.master.board[row,col+a].colour != self.colour and right != True:
                    self.legal_moves.append([row,(col+a)])                    
                    self.legal_moves_array[row,col+a] = self.master.ascii_board[row,col+a]
                right = True

            if down == False and row-a >= 0 and self.master.board[row-a,col].colour == None:
                self.legal_moves.append([row-a,col])    
                self.legal_moves_array[row-a,col] = self.master.ascii_board[row-a,col] if self.master.board[row-a,col].colour != None else "x"
            else:
                if row-a >= 0 and self.master.board[row-a,col].colour != None and self.master.board[row-a,col].colour != self.colour and down != True:
                    self.legal_moves.append([row-a,col])                    
                    self.legal_moves_array[row-a,col] = self.master.ascii_board[row-a,col]                
                down = True

            if up == False and row+a <= 7 and self.master.board[row+a,col].colour == None:
                self.legal_moves.append([row+a,col])
                self.legal_moves_array[row+a,col] = self.master.ascii_board[row+a,col] if self.master.board[row+a,col].colour != None else "x"
            else:
                if row+a <= 7 and self.master.board[row+a,col].colour != None and self.master.board[row+a,col].colour != self.colour and up != True:
                    self.legal_moves.append([row+a,col])                    
                    self.legal_moves_array[row+a,col] = self.master.ascii_board[row+a,col]                
                up = True

            a+=1
        print(self.legal_moves)
"""
