from Piece_classes import pieces as parent
import numpy as np

class Queen(parent.Piece):
    def __init__(self,master,piece,row,col,piece_type):
        super().__init__(master,piece,row,col,piece_type)

    def update_legal_moves(self):  #0.26763200759887695, 2.7*10^-4 per move max
        self.legal_moves = [[100,100]]
#        self.legal_moves_array = np.zeros((8,8),dtype=str)
        row,col = self.pos[0],self.pos[1]
        left,right,up,down,left_up,left_down,right_up,right_down,a = False,False,False,False,False,False,False,False,1

        while left==False or right==False or up==False or down==False or left_up==False or left_down==False or right_up==False or right_down==False:
            this_left = col-a
            this_right = col+a
            this_up = row-a
            this_down = row+a

            if this_left >=0:
                if left == False:
                    left = self.check_square(row,this_left,left)
                if this_up >= 0:
                    left_up = self.check_square(this_up,this_left,left_up)
                else:
                    left_up = True
                if this_down <=7:
                    left_down = self.check_square(this_down,this_left,left_down)
                else:
                    left_down = True
            else:
                left = True
                left_down = True
                left_up = True

            if this_right <=7:
                if right == False:
                    right = self.check_square(row,this_right,right)
                if this_up >= 0:
                    right_up = self.check_square(this_up,this_right,right_up)
                else:
                    right_up = True
                if this_down <=7:
                    right_down = self.check_square(this_down,this_right,right_down)
                else:
                    right_down = True
            else:
                right = True
                right_down = True
                right_up = True

            if this_down <=7:
                down = self.check_square(this_down,col,up)
            else:
                down = True

            if this_up >=0:
                up = self.check_square(this_up,col,up)
            else:
                up = True
            a+=1
        print(self.legal_moves)
                 




            
"""             if left == False and col-a >= 0 and self.master.board[row,col-a].colour == None:
                self.legal_moves = np.append(self.legal_moves,[[row,(col-a)]], axis=0)
#                 self.legal_moves_array[row,col-a] = self.master.ascii_board[row,col-a] if self.master.board[row,col-a].colour != None else "x"
            else:
                if col-a >= 0 and self.master.board[row,col-a].colour != None and self.master.board[row,col-a].colour != self.colour and left != True:
                    self.legal_moves = np.append(self.legal_moves,[[row,(col-a)]], axis=0)
    #                 self.legal_moves_array[row,col-a] = self.master.ascii_board[row,col-a]
                left = True

            if right == False and col+a <= 7 and self.master.board[row,col+a].colour == None:
                self.legal_moves = np.append(self.legal_moves,[[row,(col+a)]], axis=0)
#                 self.legal_moves_array[row,col+a] = self.master.ascii_board[row,col+a] if self.master.board[row,col+a].colour != None else "x"
            else:
                if col+a <= 7 and self.master.board[row,col+a].colour != None and self.master.board[row,col+a].colour != self.colour and right != True:
                    self.legal_moves = np.append(self.legal_moves,[[row,(col+a)]], axis=0)                  
    #                 self.legal_moves_array[row,col+a] = self.master.ascii_board[row,col+a]
                right = True

            if down == False and row-a >= 0 and self.master.board[(row-a),col].colour == None:
                self.legal_moves = np.append(self.legal_moves,[[(row-a),col]], axis=0)  
#                 self.legal_moves_array[row-a,col] = self.master.ascii_board[row-a,col] if self.master.board[row-a,col].colour != None else "x"
            else:
                if row-a >= 0 and self.master.board[row-a,col].colour != None and self.master.board[row-a,col].colour != self.colour and down != True:
                    self.legal_moves = np.append(self.legal_moves,[[(row-a),col]], axis=0)                 
    #                 self.legal_moves_array[row-a,col] = self.master.ascii_board[row-a,col]                
                down = True

            if up == False and row+a <= 7 and self.master.board[row+a,col].colour == None:
                self.legal_moves = np.append(self.legal_moves,[[(row+a),col]], axis=0)
#                 self.legal_moves_array[row+a,col] = self.master.ascii_board[row+a,col] if self.master.board[row+a,col].colour != None else "x"
            else:
                if row+a <= 7 and self.master.board[row+a,col].colour != None and self.master.board[row+a,col].colour != self.colour and up != True:
                    self.legal_moves = np.append(self.legal_moves,[[(row+a),col]], axis=0)                  
    #                 self.legal_moves_array[row+a,col] = self.master.ascii_board[row+a,col]                
                up = True
            
            if left_down == False and col-a >= 0 and row+a <=7 and self.master.board[row+a,col-a].colour == None:
                self.legal_moves = np.append(self.legal_moves,[[(row+a),(col-a)]], axis=0)
#                 self.legal_moves_array[row+a,col-a] = self.master.ascii_board[row+a,col-a] if self.master.board[row+a,col-a].colour != None else "x"
            else:
                if col-a >= 0 and row+a <=7 and self.master.board[row+a,col-a].colour != None and self.master.board[row+a,col-a].colour != self.colour and left_down == False:
                    self.legal_moves = np.append(self.legal_moves,[[(row+a),(col-a)]], axis=0)
    #                 self.legal_moves_array[row+a,col-a] = self.master.ascii_board[row+a,col-a]
                left_down = True
            
            if left_up == False and col-a >= 0 and row-a >=0 and self.master.board[row-a,col-a].colour == None:
                self.legal_moves = np.append(self.legal_moves,[[(row-a),(col-a)]], axis=0)
#                 self.legal_moves_array[row-a,col-a] = self.master.ascii_board[row-a,col-a] if self.master.board[row-a,col-a].colour != None else "x"
            else:
                if col-a >= 0 and row-a >=0 and self.master.board[row-a,col-a].colour != None and self.master.board[row-a,col-a].colour != self.colour and left_up == False:
                    self.legal_moves = np.append(self.legal_moves,[[(row-a),(col-a)]], axis=0)
    #                 self.legal_moves_array[row-a,col-a] = self.master.ascii_board[row-a,col-a]
                left_up = True

            if right_up == False and col+a <= 7 and row-a >=0 and self.master.board[row-a,col+a].colour == None:
                self.legal_moves = np.append(self.legal_moves,[[(row-a),(col+a)]], axis=0)
#                 self.legal_moves_array[row-a,col+a] = self.master.ascii_board[row-a,col+a] if self.master.board[row-a,col+a].colour != None else "x"
            else:
                if col+a <=7 and row-a >=0 and self.master.board[row-a,col+a].colour != None and self.master.board[row-a,col+a].colour != self.colour and right_up == False:
                    self.legal_moves = np.append(self.legal_moves,[[(row-a),(col+a)]], axis=0)
    #                 self.legal_moves_array[row-a,col+a] = self.master.ascii_board[row-a,col+a]
                right_up = True
            
            if right_down == False and col+a <=7 and row+a <=7 and self.master.board[row+a,col+a].colour == None:
                self.legal_moves = np.append(self.legal_moves,[[(row+a),(col+a)]], axis=0)
#                 self.legal_moves_array[row+a,col+a] = self.master.ascii_board[row+a,col+a] if self.master.board[row+a,col+a].colour != None else "x"
            else:
                if col+a <=7 and row+a <=7 and self.master.board[row+a,col+a].colour != None and self.master.board[row+a,col+a].colour != self.colour and right_down == False:
                    self.legal_moves = np.append(self.legal_moves,[[(row+a),(col+a)]], axis=0)
    #                 self.legal_moves_array[row+a,col+a] = self.master.ascii_board[row+a,col+a]
                right_down = True  

            a+=1 """

        