from gmpy2 import xmpz
import gmpy2
import numpy as np
import time
import random

def reverse_move(self): # NEEDS TO BE IMPLIMENTED
        pieces = {1: "p", 2: 'n', 3: 'b', 5: 'r', 6: 'q', 4: 'k', 9: 'P', 10: 'N', 11: 'B', 13: 'R', 14: 'Q', 12: 'K', 0: 'nothing'}
        types = {0: 'quiet', 1: 'double', 2: 'king-side', 3: 'queen-side', 4: 'capture', 5: 'ep-capture', 8: 'n-promo', 9: 'b-promo', 10: 'r-promo', 11: 'q-promo', 12: 'n-promo-capture', 13: 'b-promo-capture', 14: 'r-promo-capture', 15: 'q-promo-capture'}

        move = self.recent_moves.pop()
        if move:
            out = str(bin(move)[2:].zfill(24))
            breakdown = [pieces[int(out[:4],2)], pieces[int(out[4:8],2)], [(int(out[8:11],2)),(int(out[11:14],2))], [(int(out[14:17],2)),(int(out[17:20],2))],types[int(out[20:],2)]]
             # 0 - piece captured, 1- piece moved, 2- start square, 3- end square, 4 move type
            erow,ecol = breakdown[2]
            srow,scol = breakdown[3]
            
            
        if "promo" in breakdown[4]:
            self.board[srow,scol].destroy()
            piece = self.captured_pieces.pop()
        else:
            piece = self.board[srow,scol]
        
        self.board[erow,ecol].destroy()
        self.board[erow,ecol] = piece
        self.ascii_board[erow,ecol] = piece.ascii
        piece.grid(row=erow,column=ecol)
        piece.lift()
        piece.pos = xmpz(0)
        piece.pos[(erow<<3)+ecol] =1
        if self.piece_type in ["ascii","secret"]:
            piece.config(bg= self.colour_scheme["white"] if (erow+ecol)%2==0 else self.colour_scheme["black"])
                
        piece.has_moved -= 1
        self.half_move -= 1
        
        self.en_passant = self.old_passant
        self.old_passant = xmpz(0)
        
        if breakdown[0] == "nothing": # CHANGE TO ENCORPORTATE PROMOTE
            self.replace_piece("",tk.Label(self),[srow,scol])
        else:
            cap = self.captured_pieces.pop()
        
            self.board[srow,scol] = cap
            self.ascii_board[srow,scol] = cap.ascii
            cap.pos=xmpz(0)
            cap.pos[(srow<<3)+scol] =1
            cap.grid(row=srow,column=scol)
            cap.lift()
            if self.half_move % 2 == 0:
                self.black_positions[(srow<<3)+scol] = 1
            else:
                self.white_positions[(srow<<3)+scol] = 1
            
            cap.update_legal_moves()
        if self.half_move % 2 == 0:
            self.white_positions[(erow<<3)+ecol] = 1
            self.white_positions[(srow<<3)+scol] = 0
            self.active_colour = "w"
            
        else:
            self.active_colour ="b"
            self.full_move -= 1
            self.black_positions[(erow<<3)+ecol] = 1
            self.black_positions[(srow<<3)+scol] = 0
        
        piece.update_legal_moves()
        self.dnd.update_affected_pieces(2**(erow*8+ecol),2**(srow*8+scol))
