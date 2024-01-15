from Piece_classes import pieces as p
import numpy as np
import tkinter as tk
import time
from gmpy2 import xmpz
import math

pieces_revesed = {'♟': 'p', '♞': 'n', '♝': 'b', '♜': 'r', '♛': 'q', '♚': 'k', '♙': 'P', '♘': 'N', '♗': 'B', '♖': 'R', '♕': 'Q', '♔': 'K'}



#drag handler adds the drag functionality to all pieces by giving them these the following methods
#this allows pieces to be added dynamicaly whenever needed
class Move_handler():
    def __init__(self,master):
        self.master = master
        self.start_row,self.start_col = 0,0


    def add_dragable(self, widget):
        widget.bind("<ButtonPress-1>", self.on_start)
        widget.bind("<B1-Motion>", self.on_drag)
        widget.bind("<ButtonRelease-1>", self.on_drop)

    def get_cursor_pos(self,event):
        return min(7,max(0,(event.y_root-self.master.winfo_rooty()-self.master.border_width)//100)),min(7,max(0,(event.x_root-self.master.winfo_rootx()-self.master.border_width)//100))

    def on_start(self, event):
        #documents the starting point of the piece so it can be returned if the move is invalid
        self.start_row,self.start_col = self.get_cursor_pos(event)        
        
        
        
        if event.widget.colour == self.master.active_colour :#and self.master.piece_type != "hidden"
            if self.master.piece_type in ["ascii","secret"]:
                event.widget.config(bg="#ccff99")
            if self.master.piece_type != "secret":
                moves = bin(event.widget.legal_moves)[2:]
                for i in range(1,len(moves)+1):
                    if int(moves[-i]):
                        row,col = (i-1)//8,(i-1)%8
                        for a in self.master.grid_slaves(row =row,column =col):
                            a.config(bg=("#"+hex(int(int(self.master.colour_scheme["white"][1:],16) *0.5)%16777216).lstrip("0x")) if (row+col)%2==0 else ("#"+hex(int(int(self.master.colour_scheme["black"][1:],16)*0.5)%16777216).lstrip("0x")))
        
        
        
        
    def on_drag(self, event):
        #makes the piece follow beneath the position of the mouse on the screen by redrawing every time it moves
        event.widget.place(x=(event.x_root-self.master.winfo_rootx()-self.master.border_width),y=(event.y_root-self.master.winfo_rooty()-self.master.border_width),anchor="center")
        event.widget.lift()

    def on_drop(self, event,person =True,input = 0):
        #s = time.time()
        #locks the widget into the nearst gird space or retruns it to the starting point if it is invalid
        move = xmpz(0)
        if person:
            row,col = self.get_cursor_pos(event)
            move[(row<<3)+col] = 1
            piece = event.widget 
        else:
            row,col = min(max(0,input//8),7), min(max(0,input%8),7)
            piece = self.master.board[self.start_row,self.start_col]
            
        move[(row<<3)+col] = 1
        promo = False

        #if  self.master.piece_type != "hidden":
        moves = bin(piece.legal_moves)[2:]
        for i in range(1,len(moves)+1):
            if int(moves[-i]):
                temp_row,temp_col = (i-1)//8,(i-1)%8
                for a in self.master.grid_slaves(row =temp_row,column =temp_col):
                    a.config(bg= self.master.colour_scheme["white"] if (temp_row+temp_col)%2==0 else self.master.colour_scheme["black"])




        if  (move & piece.legal_moves) and self.master.active_colour == piece.colour:
            if self.master.piece_type in ["ascii","secret"]:
                piece.config(bg= self.master.colour_scheme["white"] if (row+col)%2==0 else self.master.colour_scheme["black"])
            
            self.master.move_stored = False
            
            if move & (self.master.white_positions | self.master.black_positions):
                move_type = "capture"
                captured = self.master.board[row,col]
                self.master.captured_pieces.push(captured)
                captured_piece= captured.ascii
                
            else:
                move_type = "quiet"
                captured_piece = '-'
                
            # updating the relevant data structures and gui
            self.update_structs(piece,(row<<3)+col)
            
            #self.get_material_diff(event)
            
            #promotion check
            if piece.ascii.lower() == "p":
                if (move & self.master.en_passant):
                    r,c = row,col

                    if self.master.half_move % 2 == 1:
                        self.master.board[r-1,c].grid_remove()
                        self.master.board[r-1,c] = p.Piece(self.master,piece='',row=self.start_row,col=self.start_col,piece_type='')
                        self.master.ascii_board[r-1,c] = ""
                        self.update_passanted(2**(((row-1)<<3)+col))
                        self.master.black_positions[((row-1)<<3)+col] = 0
                    else:
                        self.master.board[r+1,c].grid_remove()
                        self.master.board[r+1,c] = p.Piece(self.master,piece='',row=self.start_row,col=self.start_col,piece_type='')
                        self.master.ascii_board[r+1,c] = ""
                        self.update_passanted(2**(((row+1)<<3)+col))
                        self.master.black_positions[((row+1)<<3)+col] =0
                    self.master.old_passant = self.master.en_passant
                    self.master.en_passant = xmpz(0)
                    self.master.store_move([self.start_row,self.start_col],[row,col],"P","ep-capture","p")
                    print(self.master.recent_moves)
                elif not piece.has_moved and (row in [self.start_row-2,self.start_row+2]):
                    self.master.old_passant = self.master.en_passant
                    self.master.en_passant = xmpz(2**(((row-1)<<3)+col) if self.master.half_move % 2 == 1 else 2**(((row+1)<<3)+col) )
                    self.master.store_move([self.start_row,self.start_col],[row,col],piece.ascii,"double",captured_piece)
                elif ((piece.pos[0:8] ^ 0) | (piece.pos[56:64] ^ 0)):
                    self.master.promote(piece,[self.start_row,self.start_col],move_type= "promo" if move_type == "quiet" else "promo-capture",captured=captured_piece)
                    promo = True
                else:
                    self.master.old_passant = self.master.en_passant
                    self.master.en_passant = xmpz(0)
                    self.master.store_move([self.start_row,self.start_col],[row,col],piece.ascii,move_type,captured_piece)
                    
                
            else:
                self.master.old_passant = self.master.en_passant
                self.master.en_passant = xmpz(0)
                if not self.master.move_stored:
                    self.master.store_move([self.start_row,self.start_col],[row,col],piece.ascii,move_type,captured_piece)
                
            piece.has_moved +=1
            #s = time.time()
            #for i in range(10000):
            if not promo:
                self.master.half_move += 1
                self.update_affected_pieces(2**((self.start_row<<3)+self.start_col),move)
                #print((time.time()-s)/10000)

                #turn controlling
                if self.master.half_move % 2 == 1:
                    self.master.active_colour = "b"
                    if self.master.white_king.pos & self.master.black_can_take:
                        self.master.reverse_move()
                else:
                    self.master.active_colour ="w"
                    self.master.full_move += 1
                    if self.master.black_king.pos & self.master.white_can_take:
                        self.master.reverse_move()                
                
        else:
            piece.grid(row=self.start_row,column=self.start_col)
            if self.master.piece_type in ["ascii","secret"]:
                piece.config(bg= self.master.colour_scheme["white"] if (self.start_row+self.start_col)%2==0 else self.master.colour_scheme["black"])
        #print(time.time()-s)
                
    def update_structs(self,piece,move):
        row,col = move//8,move%8  
        self.master.grid_slaves(row,col)[0].destroy() if self.master.grid_slaves(row,col)[0].ascii == "" else self.master.grid_slaves(row,col)[0].grid_remove()
        
        self.master.board[row,col] = piece
        self.master.ascii_board[row,col] = piece.ascii
        piece.grid(row=row,column=col)
        piece.pos = xmpz(0)
        piece.pos[move] = 1
        
        temp = p.Piece(self.master,piece='',row=self.start_row,col=self.start_col,piece_type='')
        self.master.board[self.start_row,self.start_col] = temp
        self.master.ascii_board[self.start_row,self.start_col] = ''
        temp.grid(row=self.start_row,column=self.start_col)
        
        if self.master.half_move % 2 == 0:
            self.master.white_positions[move] = 1
            self.master.white_positions[(self.start_row<<3)+self.start_col] = 0
            self.master.black_positions[move] = 0
        else:
            self.master.black_positions[move] = 1
            self.master.black_positions[(self.start_row<<3)+self.start_col] = 0
            self.master.white_positions[move] = 0


    def update_affected_pieces(self,start,end):
        for i in self.master.piece_list:
            if (start & i.ghost_moves) | (end & i.ghost_moves):   
                i.update_legal_moves()
            elif i.ascii.lower() == "p" and ((self.master.en_passant & i.ghost_moves) | (self.master.old_passant & i.ghost_moves)) and(i.colour != ("w" if self.master.half_move % 2 == 1 else "b")):
                i.update_legal_moves()
            
        
        self.master.update_can_take("w")
        self.master.update_can_take("b")
        i.master.black_king.update_legal_moves()
        i.master.white_king.update_legal_moves()
    
    def update_passanted(self,move):
        for i in self.master.piece_list:
            if (i.ghost_moves & move):
                    i.update_legal_moves()

    def get_material_diff(self):
        w = 0
        bl = 0
        for i in self.master.white_pieces:
            w += i.value
        for i in self.master.black_pieces:
            bl+= i.value
        
        print("+"+ str((w-bl)//100)) if (w-bl) >= 0 else print("-"+ str((bl-w)//100))
    