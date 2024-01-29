import tkinter as tk

class WrappingLabel(tk.Label):
    '''a type of Label that automatically adjusts the wrap to the size'''
    def __init__(self, master=None,text="", **kwargs):
        tk.Label.__init__(self, master,text=text,font = ("arial",10),wraplength=800,justify="left",bg="#4b4b4b", **kwargs)
        self.bind('<Configure>', lambda e: self.config(wraplength=self.winfo_width()))
 