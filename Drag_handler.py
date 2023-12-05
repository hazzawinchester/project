from Piece_classes import pieces as p
import numpy as np
import tkinter as tk

pieces_revesed = {'♟': 'p', '♞': 'n', '♝': 'b', '♜': 'r', '♛': 'q', '♚': 'k', '♙': 'P', '♘': 'N', '♗': 'B', '♖': 'R', '♕': 'Q', '♔': 'K'}



#drag handler adds the drag functionality to all pieces by giving them these the following methods
#this allows pieces to be added dynamicaly whenever needed
class Drag_handler():
    def add_dragable(self, widget):
        widget.bind("<ButtonPress-1>", self.on_start)
        widget.bind("<B1-Motion>", self.on_drag)
        widget.bind("<ButtonRelease-1>", self.on_drop)

    def get_cursor_pos(self,event):
        return (event.y_root-self.master.winfo_rooty()-self.master.border_width)//100,(event.x_root-self.master.winfo_rootx()-self.master.border_width)//100

    def on_start(self, event):
        self.master = event.widget.master
        #documents the starting point of the piece so it can be returned if the move is invalid
        self.start_row,self.start_col = self.get_cursor_pos(event)
        event.widget.update_legal_moves()


        if event.widget.colour == self.master.active_colour:
            for i in event.widget.legal_moves:
                row,col = i
                for a in self.master.grid_slaves(row =row,column =col):
                    a.config(bg=("#"+hex(int(int(self.master.colour_scheme["white"][1:],16) *0.5)).lstrip("0x")) if (row+col)%2==0 else ("#"+hex(int(int(self.master.colour_scheme["black"][1:],16)*0.5)).lstrip("0x")))
        
    def on_drag(self, event):
        #makes the piece follow beneath the position of the mouse on the screen by redrawing every time it moves
        event.widget.place(x=(event.x_root-self.master.winfo_rootx()-self.master.border_width),y=(event.y_root-self.master.winfo_rooty()-self.master.border_width),anchor="center")
        event.widget.lift()

    def on_drop(self, event):
        #locks the widget into the nearst gird space or retruns it to the starting point if it is invalid
        row,col = self.get_cursor_pos(event)
        move = np.array([row,col])
        piece = event.widget    

        for i in piece.legal_moves:
            temp_row,temp_col = i
            for a in self.master.grid_slaves(row =temp_row,column =temp_col):
                a.config(bg= self.master.colour_scheme["white"] if (temp_row+temp_col)%2==0 else self.master.colour_scheme["black"])

        if (piece.legal_moves == move).all(1).any() and self.master.active_colour == piece.colour:

            self.master.grid_slaves(row,col)[0].destroy()
            piece.grid(row=row,column=col)
            temp = p.Piece(self.master,piece='',row=self.start_row,col=self.start_col,piece_type='')
            self.master.board[row,col] = piece
            self.master.board[self.start_row,self.start_col] = temp
            self.master.ascii_board[row,col] = piece.ascii
            self.master.ascii_board[self.start_row,self.start_col] = temp.ascii
            temp.grid(row=self.start_row,column=self.start_col)
            piece.pos =[row,col]
            
            self.get_material_diff(event)

            self.update_affected_pieces(event,[self.start_row,self.start_col],[row,col])

            piece.has_moved=True

            #turn controlling
            self.master.half_move += 1

            if self.master.half_move % 2 == 1:
                self.master.active_colour = "b"
            else:
                self.master.active_colour ="w"
                self.master.full_move += 1
    
            #promotion check
            if piece.ascii.lower() == "p" and (piece.pos[0] == 0 or piece.pos[0] == 7):
                self.master.promote(piece)
        else:
            piece.grid(row=self.start_row,column=self.start_col)
                

    def update_affected_pieces(self,event,start,end):
        for i in event.widget.master.piece_list:
            if (i.ghost_moves == np.array(start)).all(1).any() or (i.ghost_moves == np.array(end)).all(1).any():
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
                if self.master_board[a][b].colour == "w":
                    w += self.master_board[a][b].value
                elif self.master_board[a][b].colour == "b":
                    bl+= self.master_board[a][b].value
        print("+"+ str((w-bl)//100)) if (w-bl) >= 0 else print("-"+ str((bl-w)//100))
    