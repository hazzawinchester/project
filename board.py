import tkinter as tk
import numpy as np
import pieces as p
import Drag_handler as dh

#rows ={7:"a",6:"b",5:"c",4:"d",3:"e",2:"f",1:"g",0:"h"}
pieces = {'p':"♟︎",'n':"♞",'b':"♝",'r':"♜",'q':"♛",'k':"♚", "P":"♙", "N":"♘", "B":"♗", "R":"♖", "Q":"♕", "K":"♔"}



class chessboard(tk.Frame):
    def __init__(self, master=None,FEN=None):
        super().__init__(master)
        self.master = master
        self.grid()

        self.move_start = None

        self.dnd = dh.Drag_handler()

        self.board = np.zeros((8,8),dtype=str)
        self.make_array_of_pieces(FEN)

        self.board_background()
        self.create_widgets()

    def __str__(self):
        return f"{self.board}"

    def create_widgets(self):
        for row in range(8):
            for col in range(8):
                piece = p.Piece(self,[row,col], bg='black' , text=f"{self.board[row][col]}", font=("Arial",50), borderwidth=0)
                piece.grid(row=row, column=col)
                self.dnd.add_dragable(piece)

    def board_background(self):
        for row in range(8):
            for col in range(8):
                squares = tk.Frame(self, bg="white" if (row+col)%2==0 else "gray" ,width=100, height=100, borderwidth=0)
                squares.grid(row=row, column=col)
                #squares.bind("<Button-1>", lambda event, r=row, c=col: self.move_piece(r, c))
    
    def make_array_of_pieces(self,FEN):
        temp = FEN.split("/")
        for i in range(len(temp)):
            if temp[i].isalpha():
                self.board[i] = np.array([pieces[a] for a in temp[i]])
            elif not(temp[i].isnumeric()):
                row = []
                for a in temp[i]:
                    if a.isalpha():
                        row.append(pieces[a])
                    else:
                        for z in range(int(a)):
                            row.append('')
                self.board[i] = np.array(row)



""" def move_piece(self,r,c):
        print(self.grid_slaves(r,c)[0].position,r*8+c+1)
        if self.move_start == None:
            self.move_start = [r,c]
        else:
            self.board[r][c] = self.board[self.move_start[0]][self.move_start[1]]
            self.board[self.move_start[0]][self.move_start[1]] = ''
            
            self.grid_slaves(r,c)[0].position = [self.move_start[0],self.move_start[1]]
            print("moving to",self.grid_slaves(r,c)[0].position )
            self.grid_slaves(r,c)[0].grid(row=self.move_start[0],column=self.move_start[1]) #this works to switch the labels held in each location just the loaction is wrong
            self.grid_slaves(row=self.move_start[0],column=self.move_start[1])[1].position = [r,c]
            print("moving from", self.grid_slaves(row=self.move_start[0],column=self.move_start[1])[1].position)
            self.grid_slaves(row=self.move_start[0],column=self.move_start[1])[1].grid(row=r,column=c)

            print("end",self.grid_slaves(r,c)[0].position,"start",self.grid_slaves(row=self.move_start[0],column=self.move_start[1])[0].position)


            self.move_start = None
 """