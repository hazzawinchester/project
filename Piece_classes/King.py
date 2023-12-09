from Piece_classes import pieces as parent
from tkinter import messagebox
import numpy as np

class King(parent.Piece):
    def __init__(self,master,piece,row,col,piece_type):
        super().__init__(master,piece,row,col,piece_type)
        self.legal_moves = np.array([[100,100]])
        if piece.isupper():
            self.master.white_king = self
        else:
            self.master.black_king = self

    def destroy(self):
        super().destroy()
        #if self.game_over == False:
        #    messagebox.showinfo(title="Winner!", message="black has won" if self.colour == "w" else "white has won", parent=self.master.master)
        #    self.game_over = True

    def update_legal_moves(self):
        self.ghost_moves =[[100,100]]
        self.legal_moves = [[100,100]]
        row,col = self.pos

        for r in range(-1,2):
            for c in range(-1,2):
                r_new = row+r
                c_new = col+c
                if r_new ==row and c_new == col:
                    continue
                if self.colour == "w":
                    if not ((self.master.black_can_take == [r_new,c_new]).all(1).any()):
                        if r_new // 8 == 0 and c_new // 8 == 0:
                            self.check_square(r_new,c_new)
                    else:
                        self.ghost_moves = np.append(self.ghost_moves,[[r_new,c_new]],axis=0)
                else:
                    if not ((self.master.white_can_take == [r_new,c_new]).all(1).any()):
                        if r_new // 8 == 0 and c_new // 8 == 0:
                            self.check_square(r_new,c_new)
                    else:
                        self.ghost_moves = np.append(self.ghost_moves,[[r_new,c_new]],axis=0)