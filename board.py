import tkinter as tk
import numpy as np
from Piece_classes import pieces as p
import Drag_handler as dh
from Piece_classes import Pawn,Bishop,Knight,Rook,Queen,King
from Stack import Stack 



#rows ={7:"a",6:"b",5:"c",4:"d",3:"e",2:"f",1:"g",0:"h"}
# allows to translate between the ascii and aplhabetical represntation of each piece

binary = {"a":7,"b":6,"c":5,"d":4, "e":3, "f":2, "g":1, "h":0}

# board class which will be used to create a chessboard from a given FEN string, is a child of tk.frame so it can contain the gui function of the board
class chessboard(tk.Frame):
    def __init__(self, master=None,FEN="rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1",piece_type="classic", game_type="2p", colour_scheme=["#e2bd8d","#421e00"], border_width = 35):
        super().__init__(master,borderwidth=border_width, bg=colour_scheme[1])
        self.pieces = {'p':"♟",'n':"♞",'b':"♝",'r':"♜",'q':"♛",'k':"♚", "P":"♙", "N":"♘", "B":"♗", "R":"♖", "Q":"♕", "K":"♔"}
        self.pieces_revesed = {'♟': 'p', '♞': 'n', '♝': 'b', '♜': 'r', '♛': 'q', '♚': 'k', '♙': 'P', '♘': 'N', '♗': 'B', '♖': 'R', '♕': 'Q', '♔': 'K'}

        self.binary = {"a":7,"b":6,"c":5,"d":4, "e":3, "f":2, "g":1, "h":0}
        self.binary_reversed = {0: 'h', 1: 'g', 2: 'f', 3: 'e', 4: 'd', 5: 'c', 6: 'b', 7: 'a'}

        self.master = master
        self.move_start=None
        self.piece_type = piece_type
        self.game_type = game_type
        self.move_stored = False
    
        self.border_width =border_width
        self.recent_moves = Stack()

        white = colour_scheme[0]
        black =colour_scheme[1]
        self.colour_scheme = {"white": white, "black": black}

        self.piece_list = []
        self.white_pieces = []
        self.black_pieces = []    
        self.black_king = None
        self.white_king = None   

        self.dnd = dh.Drag_handler()

        
        self.ascii_board = np.zeros((8,8),dtype=str)
        self.FEN_extractor(FEN)
        self.board_background()

        self.create_widgets()

        self.board  = np.array([[self.grid_slaves()[-(65+(8*a+i))] for i in range(8)] for a in range(8)])
        self.set_all_piece_moves()
        
        self.white_can_take = [[100,100]]
        self.black_can_take = [[100,100]]
        self.update_can_take("w")
        self.update_can_take("b")
        self.white_king.update_legal_moves()
        self.black_king.update_legal_moves()
        
        self.bind('<Return>', self.reverse_move)
        
    def __str__(self): 
        return f"{self.convert_into_fen()}"
    
    def destroy(self):
        print(self.convert_into_fen())
        super().destroy()
        
    def create_widgets(self):
        for row in range(8):
            for col in range(8):
                temp = self.ascii_board[row][col]
                if temp == '':
                    piece = p.Piece(self,temp,row,col,self.piece_type)
                else:
                    if temp.lower() == "p":
                        piece = Pawn.Pawn(self,temp,row,col,self.piece_type)
                    elif temp.lower() == "n":
                        piece = Knight.Knight(self,temp,row,col,self.piece_type)                    
                    elif temp.lower() == "b":
                        piece = Bishop.Bishop(self,temp,row,col,self.piece_type)   
                    elif temp.lower() == "r":
                        piece = Rook.Rook(self,temp,row,col,self.piece_type)       
                    elif temp.lower() == "q":
                        piece = Queen.Queen(self,temp,row,col,self.piece_type)  
                    elif temp.lower() == "k":
                        piece = King.King(self,temp,row,col,self.piece_type)  

                    if temp.isupper():
                        self.white_pieces = np.append(self.white_pieces,piece)
                    else:
                        self.black_pieces = np.append(self.black_pieces,piece)

                    self.piece_list = np.append(self.piece_list,piece)
                                                                             
                piece.grid(row=row, column=col)
                self.dnd.add_dragable(piece)
    
    def set_all_piece_moves(self):
        save=[]
        for i in self.piece_list:
            if i.ascii.lower() != "k":
                i.update_legal_moves()
        

    #creates a 8*8 grid of coloured squares to serve as the board being played on
    def board_background(self):
        white = self.colour_scheme["white"]
        black = self.colour_scheme["black"]
        for row in range(8):
            for col in range(8):
                squares = tk.Frame(self, bg= white if (row+col)%2==0 else black ,width=100, height=100, borderwidth=4)
                squares.grid(row=row, column=col)
    
    #translates the FEN string into a 2D array of the pieces in ther respective positions (black at the top/start of the array)
    def make_array_of_pieces(self,board):
        temp = board.split("/")
        for i in range(8):
            if temp[i].isalpha():
                self.ascii_board[i] = np.array([a for a in temp[i]])
            elif not(temp[i].isnumeric()):
                row = []
                for a in temp[i]:
                    if a.isalpha():
                        row.append(a)
                    else:
                        for z in range(int(a)):
                            row.append('')
                self.ascii_board[i] = np.array(row)

    def update_can_take(self,colour):
        if colour == "b":
            self.black_can_take = [[100,100]]
            for i in self.black_pieces:
                if i.ascii == "k":
                    self.black_can_take = np.unique(np.concatenate((self.black_can_take,i.ghost_moves),axis=0),axis=0)
                if i.ascii == "p":
                    if i.pos[1] in [0,7]:
                        self.black_can_take = np.unique(np.concatenate((self.black_can_take,i.ghost_moves[-1:]),axis=0),axis=0)
                    else:
                        self.black_can_take = np.unique(np.concatenate((self.black_can_take,i.ghost_moves[-2:]),axis=0),axis=0)
                else:
                    self.black_can_take = np.unique(np.concatenate((self.black_can_take,i.ghost_moves),axis=0),axis=0)
        else:
            self.white_can_take = [[100,100]]
            for i in self.white_pieces:
                if i.ascii == "K":
                    self.white_can_take = np.unique(np.concatenate((self.white_can_take,i.ghost_moves),axis=0),axis=0)
                elif i.ascii == "P":
                    if i.pos[1] in [0,7]:
                        self.white_can_take = np.unique(np.concatenate((self.white_can_take,i.ghost_moves[-1:]),axis=0),axis=0)
                    else:
                        self.white_can_take = np.unique(np.concatenate((self.white_can_take,i.ghost_moves[-2:]),axis=0),axis=0)
                else:
                    self.white_can_take = np.unique(np.concatenate((self.white_can_take,i.ghost_moves),axis=0),axis=0)




    #converts the move into a unique integer that is added to the stack so it can be reversed at any time
    def store_move(self,start,end,piece,type="quiet",captured="-"):
        if not self.move_stored:
            convert = {"p":1,"n":2,"b":3,"r":5,"q":6,"k":4,"P":9,"N":10,"B":11,"R":13,"Q":14,"K":12, "-":0}
            move_types = {'quiet': 0, 'double': 1, 'pawn': 1, 'push': 1, 'king-side': 2, 'queen-side': 3, 'capture': 4, 'ep-capture': 5, 'n-promo': 8, 'b-promo': 9, 'r-promo': 10, 'q-promo': 11, 'n-promo-capture': 12, 'b-promo-capture': 13, 'r-promo-capture': 14, 'q-promo-capture': 15}
            move =(convert[captured] << 20) + (convert[piece] <<16)+(((start[0]*8) + start[1]) <<10)+(((end[0]*8) + end[1]<<4)) +move_types[type]
            self.recent_moves.push(move) # this is very ugly should be fixed
            self.move_stored = True
            self.recent_moves.peak()
        else:
            print("oh no no")
        
        
        
        
        
    
    def reverse_move(self): # NEEDS TO BE IMPLIMENTED
        move = self.recent_moves.pop()
        print(move)
        pass
    
    def FEN_extractor(self,fen):
        fen = fen.split(" ")
        self.make_array_of_pieces(fen[0])
        self.active_colour = fen[1]
        self.avaiable_castle = fen[2]
        self.en_passent = np.array(self.convert_from_binary(fen[3]))
        self.half_move = int(fen[4])
        self.full_move = int(fen[5])

    def convert_into_fen(self):
        board = ""
        count = 0
        for i in self.ascii_board:
            temp = ""
            for a in range(len(i)):
                if i[a] == '' :
                    count+= 1
                    if a == 7:
                        temp += str(count)
                        count = 0
                elif count > 0:
                    temp += str(count) + i[a]
                    count = 0
                else:
                    temp += i[a]
            board += temp + "/"
        board = board[:-1]
        
        return f"{board} {self.active_colour} {self.avaiable_castle} {self.convert_to_binary(self.en_passent)} {self.half_move} {self.full_move}"
    
    def convert_from_binary(self,move):
        if move == '-':
            return [200,100]
        return [int(move[1])-1,self.binary[move[0]]]
    
    def convert_to_binary(self,move):
        if (move == [200,100]).all(0).any():
            return "-"
        return self.binary_reversed[move[0]] + str(move[1]+1)
        
    

    
# once a pawn has reached the last rank it is deleted and the user is offered 4 options between for which piece they would like to promote to 
    def promote(self,piece,start,move_type=None,captured="-"):
        self.move_stored = True
        row,col = piece.pos
        container = tk.Frame(self,width=100,height=100, bg="white" if (row+col)%2==0 else "gray", borderwidth=0,padx=0,pady=0)
        container.grid_columnconfigure(col, minsize=2)
        container.grid_rowconfigure(row, minsize=2)

        container.grid(row=row,column=col)

        piece.destroy()

        self.active_colour = None

        tk.Button(container, bg= self.colour_scheme["white"], text="♛", font=["arial",15], command= lambda:[ self.replace_piece("q",container,[row,col]), self.store_move(start,[row,col],piece.ascii,"q-"+move_type,captured)]).grid(row=0,column=0, sticky= "nesw")
        tk.Button(container, bg= self.colour_scheme["black"], text="♜" ,font=["arial",15], command= lambda:[ self.replace_piece("r",container,[row,col]), self.store_move(start,[row,col],piece.ascii,"r-"+move_type,captured)]).grid(row=0,column=1, sticky= "nesw")
        tk.Button(container, bg= self.colour_scheme["black"], text="♝", font=["arial",15], command= lambda:[ self.replace_piece("b",container,[row,col]), self.store_move(start,[row,col],piece.ascii,"b-"+move_type,captured)]).grid(row=1,column=0, sticky= "nesw")
        tk.Button(container, bg= self.colour_scheme["white"], text="♞", font=["arial",15], command= lambda:[ self.replace_piece("n",container,[row,col]), self.store_move(start,[row,col],piece.ascii,"n-"+move_type,captured)]).grid(row=1,column=1, sticky= "nesw")

        # places a piece in the position of the pawn and corrects all the data structures to refelct this
    def replace_piece(self,p,container,pos):
        
        self.move_stored = False # essential as otherwise the program runs too fast in the drag handler and treats it as just a normal capture
        
        row,col = pos
        if row == 0:
            piece_ascii = p.upper()
        else:
            piece_ascii = p

        if p == "q":
            piece = Queen.Queen(self,piece_ascii,row,col,self.piece_type)
        elif p == "r":
            piece = Rook.Rook(self,piece_ascii,row,col,self.piece_type)
        elif p == "n":
            piece = Knight.Knight(self,piece_ascii,row,col,self.piece_type)
        elif p == "b":
            piece = Bishop.Bishop(self,piece_ascii,row,col,self.piece_type)   
        
        self.ascii_board[row,col] = piece_ascii
        self.board[row,col] = piece
        self.piece_list = np.append(self.piece_list,piece)

        if piece_ascii.isupper():
            self.white_pieces = np.append(self.white_pieces,piece)
        else:
            self.black_pieces = np.append(self.black_pieces,piece)
        
        piece.update_legal_moves()

        piece.grid(row=row,column=col)
        self.dnd.add_dragable(piece)

        container.destroy()

        self.active_colour = "w" if row ==7 else "b"




    
    


