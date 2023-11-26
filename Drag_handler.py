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
        self.master = event.widget.master
        #documents the starting point of the piece so it can be returned if the move is invalid
        self.start_row,self.start_col = (event.y_root-self.master.winfo_rooty())//100,(event.x_root-self.master.winfo_rootx())//100
        event.widget.update_legal_moves()
        #self.display_possible_moves(event)

    def on_drag(self, event):
        #makes the piece follow beneath the position of the mouse on the screen by redrawing every time it moves
        event.widget.place(x=(event.x_root-self.master.winfo_rootx()),y=(event.y_root-self.master.winfo_rooty()),anchor="center")
        event.widget.lift()

    def on_drop(self, event):
        #locks the widget into the nearst gird space or retruns it to the starting point if it is invalid
        row,col = (event.y_root-self.master.winfo_rooty())//100,(event.x_root-self.master.winfo_rootx())//100
        move = np.array([row,col])
        if (event.widget.legal_moves == move).all(1).any():

            self.master.grid_slaves(row,col)[0].destroy()
            event.widget.grid(row=row,column=col)

            # .baord[colum,row]
            temp = p.Piece(self.master,piece='',row=self.start_row,col=self.start_col,piece_type='')
            self.master.board[row,col] = event.widget
            self.master.board[self.start_row,self.start_col] = temp
            self.master.ascii_board[row,col] = event.widget.ascii
            self.master.ascii_board[self.start_row,self.start_col] = temp.ascii
            temp.grid(row=self.start_row,column=self.start_col)

            event.widget.pos =[row,col]

            self.get_material_diff(event)

            #self.get_ghost_moves(event,[self.start_row,self.start_col],[row,col])
            #event.widget.update_moves()

            event.widget.has_moved=True

            
        else:
            event.widget.grid(row=self.start_row,column=self.start_col)

    def get_ghost_moves(self,event,start,end):
        event.widget.update_ghost_moves()
        for i in event.widget.master.piece_list:
            if (i.legal_moves == np.array(start)).all(1).any() or (i.legal_moves == np.array(end)).all(1).any():
                i.update_legal_moves()

    def display_possible_moves(self,event):
        for i in event.widget.legal_moves:
            if (i == np.array([100,100])).any():
                continue
            #event.widget.master.gridslaves(row =i[0],column =i[1])[0].config(bg ="red")

    def get_material_diff(self,event):
        w = 0
        bl = 0
        self.master_board = event.widget.master.board
        for a in range(8):
            for b in range(8):
                if self.master[a][b].colour == "w":
                    w += self.master[a][b].value
                elif self.master[a][b].colour == "b":
                    bl+= self.master[a][b].value
        print("+"+ str((w-bl)//100)) if (w-bl) >= 0 else print("-"+ str((bl-w)//100))