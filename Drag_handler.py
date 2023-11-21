import tkinter as tk
from Piece_classes import pieces as p
from Piece_classes import Pawn,Bishop,Knight,Rook,Queen,King
import numpy as np

pieces_revesed = {'♟': 'p', '♞': 'n', '♝': 'b', '♜': 'r', '♛': 'q', '♚': 'k', '♙': 'P', '♘': 'N', '♗': 'B', '♖': 'R', '♕': 'Q', '♔': 'K'}



#drag handler adds the drag functionality to all pieces by giving them these the following methods
#this allows pieces to be added dynamicaly whenever needed
class Drag_handler():
    def add_dragable(self, widget):
        widget.bind("<ButtonPress-1>", self.on_start)
        widget.bind("<B1-Motion>", self.on_drag)
        widget.bind("<ButtonRelease-1>", self.on_drop)

    def on_start(self, event):
        #documents the starting point of the piece so it can be returned if the move is invalid
        self.start_row,self.start_col = (event.y_root-event.widget.master.winfo_rooty())//100,(event.x_root-event.widget.master.winfo_rootx())//100
        event.widget.update_legal_moves()

    def on_drag(self, event):
        #makes the piece follow beneath the position of the mouse on the screen by redrawing every time it moves
        event.widget.place(x=(event.x_root-event.widget.master.winfo_rootx()),y=(event.y_root-event.widget.master.winfo_rooty()),anchor="center")
        event.widget.lift()

    def on_drop(self, event):
        #locks the widget into the nearst gird space or retruns it to the starting point if it is invalid
        row,col = (event.y_root-event.widget.master.winfo_rooty())//100,(event.x_root-event.widget.master.winfo_rootx())//100
        #if (row != self.start_row or col!= self.start_col )and row<8 and col<8 and row>=0 and col>=0 and (event.widget.colour != event.widget.master.grid_slaves(row,col)[0].colour):
        if (event.widget.legal_moves == np.array([row,col])).all(1).any():

            event.widget.master.grid_slaves(row,col)[0].destroy()
            event.widget.grid(row=row,column=col)


            # .baord[colum,row]
            temp = p.Piece(event.widget.master,piece='',row=self.start_row,col=self.start_col,piece_type='')
            event.widget.master.board[row,col] = event.widget
            event.widget.master.board[self.start_row,self.start_col] = temp
            event.widget.master.ascii_board[row,col] = event.widget.ascii
            event.widget.master.ascii_board[self.start_row,self.start_col] = temp.ascii
            temp.grid(row=self.start_row,column=self.start_col)

            event.widget.pos =[row,col]

            self.get_material_diff(event)
            #print(event.widget)
            #event.widget.update_moves()

            event.widget.has_moved=True
        else:
            event.widget.grid(row=self.start_row,column=self.start_col)

    def get_material_diff(self,event):
        w = 0
        bl = 0
        for a in range(8):
            for b in range(8):
                if event.widget.master.board[a][b].colour == "w":
                    w += event.widget.master.board[a][b].value
                elif event.widget.master.board[a][b].colour == "b":
                    bl+= event.widget.master.board[a][b].value
        print("+"+ str((w-bl)//100)) if (w-bl) >= 0 else print("-"+ str((bl-w)//100))