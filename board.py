import tkinter as tk
import numpy as np
import pieces as p
import Drag_handler as dh

#rows ={7:"a",6:"b",5:"c",4:"d",3:"e",2:"f",1:"g",0:"h"}
# allows to translate between the ascii and aplhabetical represntation of each piece
pieces = {'p':"♟",'n':"♞",'b':"♝",'r':"♜",'q':"♛",'k':"♚", "P":"♙", "N":"♘", "B":"♗", "R":"♖", "Q":"♕", "K":"♔"}
pieces_revesed = {'♟': 'p', '♞': 'n', '♝': 'b', '♜': 'r', '♛': 'q', '♚': 'k', '♙': 'P', '♘': 'N', '♗': 'B', '♖': 'R', '♕': 'Q', '♔': 'K'}


# board class which will be used to create a chessboard from a given FEN string, is a child of tk.frame so it can contain the gui function of the board
class chessboard(tk.Frame):
    def __init__(self, master=None,FEN="rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR",piece_type="classic"):
        super().__init__(master)

        #makes the instance a grid so the board can be placed inside
        self.grid()

        self.master = master
        self.move_start=None
        self.piece_type = piece_type

        # creates a drag handler which is used to add the drag funcionality to a piece
        self.dnd = dh.Drag_handler()

        #creates an 2D array of the current board state which can be used for testing and output if no image is availbe for the piece
        self.ascii_board = np.zeros((8,8),dtype=str)
        self.make_array_of_pieces(FEN)

        #creates the background coloured squares of the chessboard
        self.board_background()

        # creates all of the pieces based off the ascii represntation of the board
        self.create_widgets()

        #creates a 2D array of all piece objects in their respective positions
        self.board  = np.array([[self.grid_slaves()[8*a+i] for i in range(8)] for a in range(8)])

    def __str__(self): # if chessboard is printed in an emergancy it will output the ascii reprpresntation of the board
        return f"{self.ascii_board}"


    # not finished will have added functionality based on pieces
    def create_widgets(self):
        for row in range(8):
            for col in range(8):
                piece = p.Piece(self,self.ascii_board[row][col],row,col,self.piece_type)
                piece.grid(row=row, column=col)
                self.dnd.add_dragable(piece)

    #creates a 8*8 grid of coloured squares to serve as the board being played on
    def board_background(self,white="white",black="gray"):
        for row in range(8):
            for col in range(8):
                #for each sqaure on the 8*8 board creates a coloured frame
                squares = tk.Frame(self, bg=white if (row+col)%2==0 else black ,width=100, height=100, borderwidth=0)

                # places each square in its position in the grid of chessboard
                squares.grid(row=row, column=col)
    
    #translates the FEN string into a 2D array of the pieces in ther respective positions (black at the top/start of the array)
    def make_array_of_pieces(self,FEN):
        temp = FEN.split("/")
        for i in range(len(temp)):
            if temp[i].isalpha():
                self.ascii_board[i] = np.array([pieces[a] for a in temp[i]])
            elif not(temp[i].isnumeric()):
                row = []
                for a in temp[i]:
                    if a.isalpha():
                        row.append(pieces[a])
                    else:
                        for z in range(int(a)):
                            row.append('')
                self.ascii_board[i] = np.array(row)

