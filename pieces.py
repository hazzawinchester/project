import tkinter as tk

class Piece(tk.Label):
    def __init__(self,master,pos,bg=None,text=None,font=None,borderwidth=None):
        super().__init__(master,text=text,bg=bg,font=font,borderwidth=borderwidth)
        self.master=master
        self.position = pos