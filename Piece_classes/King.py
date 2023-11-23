from Piece_classes import pieces as parent
from tkinter import messagebox
import numpy as np

class King(parent.Piece):
    def __init__(self,master,piece,row,col,piece_type):
        super().__init__(master,piece,row,col,piece_type)
        self.game_over = False
        self.legal_moves = np.array([[100,100]])

    def destroy(self):
        super().destroy()
        if self.game_over == False:
            messagebox.showinfo(title="Winner!", message="black has won" if self.colour == "w" else "white has won", parent=self.master.master)
            self.game_over = True

    def update_legal_moves(self):
        pass