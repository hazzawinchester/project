import tkinter as tk
from PIL import ImageTk, Image
import numpy as np
from functools import lru_cache


pieces = {'p':"♟",'n':"♞",'b':"♝",'r':"♜",'q':"♛",'k':"♚", "P":"♙", "N":"♘", "B":"♗", "R":"♖", "Q":"♕", "K":"♔", '':''}
file_type = {"classic":"png","periodic":"png", "hidden":"png"}
values = {"p":100,"n":305,"b":333,"r":563,"q":950,"k":0,'':0}


#https://en.wikipedia.org/wiki/Chess_piece_relative_value#:~:text=The%20best%20known%20system%20assigns,piece%20is%20very%20position%20dependent.

#https://thenounproject.com FOR ICONS 
# https://www.photopea.com to create images
# piece parent class to all pieces, contains no functionality as each piece is unique 

class Piece(tk.Label):
    def __init__(self,master,piece,row,col,piece_type):
        # '' is used to hold an empty sqaure

        if piece != '':
            if piece_type == "ascii":   
                super().__init__(master,text = pieces[piece], font= ["arial",50], borderwidth=0,bg=master.colour_scheme["white"] if (row+col)%2==0 else master.colour_scheme["black"])
                if piece.isupper():
                    self.colour = "w"
                else:
                    self.colour = "b"
                    
            elif piece_type == "hidden":
                if piece.isupper():
                    # fetches the white image corelating to the piece
                    self.img = Image.open(f"Pieces_img/{piece_type}/{piece_type}.{file_type[piece_type]}")
                    self.colour ="w"
                else: 
                    #fetches the black image corelating to the piece
                    self.img = Image.open(f"Pieces_img/{piece_type}/{piece_type}.{file_type[piece_type]}")
                    self.colour = "b"
                self.img = self.img.resize((75, 75))
                self.img = ImageTk.PhotoImage(self.img)
                super().__init__(master,borderwidth=0,image=self.img,bg="gray")
            else:
                #checks if the pieces is white (.isupper() will be True)
                if piece.isupper():
                    # fetches the white image corelating to the piece
                    self.img = Image.open(f"Pieces_img/{piece_type}/{piece_type}w{piece.lower()}.{file_type[piece_type]}")
                    self.colour ="w"
                else: 
                    #fetches the black image corelating to the piece
                    self.img = Image.open(f"Pieces_img/{piece_type}/{piece_type}b{piece}.{file_type[piece_type]}")
                    if master.game_type =="2p":
                        self.img = self.img.transpose(Image.ROTATE_180)
                    self.colour = "b"
                    
                #sets the image to a standard size and applys it to the object    
                self.img = self.img.resize((90, 90))
                self.img = ImageTk.PhotoImage(self.img)
                super().__init__(master,borderwidth=0,image=self.img,bg="gray")
        else:
            #used for empty squares so operations can be generalised to be performed on tk.lable objects
            super().__init__(master,borderwidth=0,bg=master.colour_scheme["white"] if (row+col)%2==0 else master.colour_scheme["black"])
            self.colour = None

        # piece attributes
        self.master = master
        self.pos = [row,col]
        self.ascii = piece
        self.value = values[piece.lower() if piece != '' else '']
        self.has_moved = False
        self.legal_moves = [[100,100]]
        self.ghost_moves = [[100,100]]
        
    def __str__(self):
        rows ={7:"a",6:"b",5:"c",4:"d",3:"e",2:"f",1:"g",0:"h"}
        return f"{self.ascii},{self.colour},{rows[self.pos[0]],self.pos[1]+1}"
    
    def destroy(self):
        super().destroy()
        if self.ascii != '':
            self.master.piece_list = np.delete(self.master.piece_list, np.where(self.master.piece_list == self))
            if self.colour == "w":
                self.master.white_pieces = np.delete(self.master.white_pieces, np.where(self.master.white_pieces == self))
            else:
                self.master.black_pieces = np.delete(self.master.black_pieces, np.where(self.master.black_pieces == self))

    
    def update_legal_moves(self):
        pass
    def update_ghost_moves(self):
        pass

    def check_square(self,row,col,found= False):
            if self.master.board[row,col].colour == None and found == False:
                self.legal_moves = np.append(self.legal_moves,[[row,col]], axis=0)
                self.ghost_moves = np.append(self.ghost_moves,[[row,col]], axis=0)
                return False
            else:
                if self.master.board[row,col].colour != self.colour and found == False:
                    self.legal_moves = np.append(self.legal_moves,[[row,col]], axis=0)
                    self.ghost_moves = np.append(self.ghost_moves,[[row,col]], axis=0)
                if self.master.board[row,col].colour == self.colour:
                    self.ghost_moves = np.append(self.ghost_moves,[[row,col]], axis=0)
                return True