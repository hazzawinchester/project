from Piece_classes import pieces as p
import numpy as np
import tkinter as tk
import time
from gmpy2 import xmpz

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
        
        
        
        
        # if event.widget.colour == self.master.active_colour :#and self.master.piece_type != "hidden"
        #     if self.master.piece_type in ["ascii","secret"]:
        #         event.widget.config(bg="#ccff99")
        #     if self.master.piece_type != "secret":
        #         for i in event.widget.legal_moves:
        #             row,col = i
        #             for a in self.master.grid_slaves(row =row,column =col):
        #                 a.config(bg=("#"+hex(int(int(self.master.colour_scheme["white"][1:],16) *0.5)%16777216).lstrip("0x")) if (row+col)%2==0 else ("#"+hex(int(int(self.master.colour_scheme["black"][1:],16)*0.5)%16777216).lstrip("0x")))
        
        
        
        
    def on_drag(self, event):
        #makes the piece follow beneath the position of the mouse on the screen by redrawing every time it moves
        event.widget.place(x=(event.x_root-self.master.winfo_rootx()-self.master.border_width),y=(event.y_root-self.master.winfo_rooty()-self.master.border_width),anchor="center")
        event.widget.lift()

    def on_drop(self, event):
        #s = time.time()
        #locks the widget into the nearst gird space or retruns it to the starting point if it is invalid
        row,col = self.get_cursor_pos(event)
        move = 2**(row*8+col)
        piece = event.widget 

        #if  self.master.piece_type != "hidden":
        # for i in piece.legal_moves:
        #     temp_row,temp_col = i
        #     for a in self.master.grid_slaves(row =temp_row,column =temp_col):
        #         a.config(bg= self.master.colour_scheme["white"] if (temp_row+temp_col)%2==0 else self.master.colour_scheme["black"])




        if  (move & piece.legal_moves) and self.master.active_colour == piece.colour: #(piece.legal_moves == move).all(1).any()
            
            if self.master.piece_type in ["ascii","secret"]:
                piece.config(bg= self.master.colour_scheme["white"] if (row+col)%2==0 else self.master.colour_scheme["black"])
            
            self.master.move_stored = False
            
            if self.master.ascii_board[row,col] != '':
                move_type = "capture"
                captured = self.master.board[row,col]
                self.master.captured_pieces.push(captured)
                captured_piece= captured.ascii
                
            else:
                move_type = "quiet"
                captured_piece = '-'
                
            # updating the relevant data structures and gui
            self.update_structs(piece,[row,col])
            
            #self.get_material_diff(event)
            
            #promotion check
            if piece.ascii.lower() == "p":
                if (move & self.master.en_passent):
                    r,c = row,col

                    if self.master.half_move % 2 == 1:
                        self.master.board[r-1,c].grid_remove()
                        self.master.board[r-1,c] = p.Piece(self.master,piece='',row=self.start_row,col=self.start_col,piece_type='')
                        self.update_passented(event,2**((row-1)*8+col))
                        self.master.store_move([self.start_row,self.start_col],[row,col],"p","ep-capture","P")
                    else:
                        self.master.board[r+1,c].grid_remove()
                        self.master.board[r+1,c] = p.Piece(self.master,piece='',row=self.start_row,col=self.start_col,piece_type='')
                        self.update_passented(event,2**((row+1)*8+col))
                        self.master.store_move([self.start_row,self.start_col],[row,col],"P","ep-capture","p")
                elif not piece.has_moved and (row in [self.start_row-2,self.start_row+2]):
                    self.master.old_passent = self.master.en_passent
                    self.master.en_passent = xmpz(2**((row-1)*8+col) if self.master.half_move % 2 == 1 else 2**((row+1)*8+col) )
                    self.master.store_move([self.start_row,self.start_col],[row,col],piece.ascii,"double",captured_piece)
                else:
                    self.master.old_passent = self.master.en_passent
                    self.master.en_passent = xmpz(0)
                    self.master.store_move([self.start_row,self.start_col],[row,col],piece.ascii,move_type,captured_piece)
                    
                if (piece.pos[0] == 0 or piece.pos[0] == 7):
                    self.master.promote(piece,[self.start_row,self.start_col],move_type= "promo" if move_type == "quiet" else "promo-capture",captured=captured_piece)
            else:
                self.master.old_passent = self.master.en_passent
                self.master.en_passent = xmpz(0)
                if not self.master.move_stored:
                    self.master.store_move([self.start_row,self.start_col],[row,col],piece.ascii,move_type,captured_piece)
                
            piece.has_moved +=1
            
            self.master.half_move += 1
            s = time.time()
            for i in range(10000):
                self.update_affected_pieces(2**(self.start_row*8+self.start_col),2**(row*8+col))
            print((time.time()-s)/10000)

            #turn controlling
            if self.master.half_move % 2 == 1:
                self.master.active_colour = "b"
                if (2**(self.master.white_king.pos[0]*8+self.master.white_king.pos[1])) & self.master.black_can_take:
                    self.master.reverse_move()
            else:
                self.master.active_colour ="w"
                self.master.full_move += 1
                if (2**(self.master.black_king.pos[0]*8+self.master.black_king.pos[1])) & self.master.white_can_take:
                    self.master.reverse_move()
                    pass
                
            
                
        else:
            piece.grid(row=self.start_row,column=self.start_col)
            if self.master.piece_type in ["ascii","secret"]:
                piece.config(bg= self.master.colour_scheme["white"] if (self.start_row+self.start_col)%2==0 else self.master.colour_scheme["black"])
        #print(time.time()-s)
                
    def update_structs(self,piece,move):
        row,col = move
        self.master.grid_slaves(row,col)[0].destroy() if self.master.grid_slaves(row,col)[0].ascii == "" else self.master.grid_slaves(row,col)[0].grid_remove()
        
        self.master.board[row,col] = piece
        self.master.ascii_board[row,col] = piece.ascii
        piece.grid(row=row,column=col)
        piece.pos =[row,col]
        
        temp = p.Piece(self.master,piece='',row=self.start_row,col=self.start_col,piece_type='')
        self.master.board[self.start_row,self.start_col] = temp
        self.master.ascii_board[self.start_row,self.start_col] = ''
        temp.grid(row=self.start_row,column=self.start_col)


    def update_affected_pieces(self,start,end):
        for i in self.master.piece_list:
            if (start & i.ghost_moves) | (end & i.ghost_moves):   
                i.update_legal_moves()
            elif i.ascii.lower() == "p" and ((self.master.en_passent & i.ghost_moves) | (self.master.old_passent & i.ghost_moves)) and(i.colour != ("w" if self.master.half_move % 2 == 1 else "b")):
                i.update_legal_moves()
            
        
        self.master.update_can_take("w")
        self.master.update_can_take("b")
        i.master.black_king.update_legal_moves()
        i.master.white_king.update_legal_moves()
    
    def update_passented(self,event,move):
        for i in event.widget.master.piece_list:
            if (i.ghost_moves & move):
                    i.update_legal_moves()

    def get_material_diff(self,event):
        w = 0
        bl = 0
        master = event.widget.master
        for i in master.white_pieces:
            w += i.value
        for i in master.black_pieces:
            bl+= i.value
        
        print("+"+ str((w-bl)//100)) if (w-bl) >= 0 else print("-"+ str((bl-w)//100))
    