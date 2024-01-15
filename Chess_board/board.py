import tkinter as tk
import numpy as np
from Piece_classes import pieces,Pawn,Bishop,Knight,Rook,Queen,King
from Chess_board import Stack,Move_handler
from gmpy2 import xmpz
import math
import time
import random




binary = {"a":7,"b":6,"c":5,"d":4, "e":3, "f":2, "g":1, "h":0}

# board class which will be used to create a chessboard from a given FEN string, is a child of tk.frame so it can contain the gui function of the board
class chessboard(tk.Frame):
    def __init__(self, master=None,FEN="rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1",stack=[],piece_type="classic", game_type="2p", colour_scheme=["#e2bd8d","#421e00"], border_width = 35):
        super().__init__(master,borderwidth=border_width, bg=colour_scheme[1])
        self.pieces = {'p':"♟",'n':"♞",'b':"♝",'r':"♜",'q':"♛",'k':"♚", "P":"♙", "N":"♘", "B":"♗", "R":"♖", "Q":"♕", "K":"♔"}
        self.pieces_revesed = {'♟': 'p', '♞': 'n', '♝': 'b', '♜': 'r', '♛': 'q', '♚': 'k', '♙': 'P', '♘': 'N', '♗': 'B', '♖': 'R', '♕': 'Q', '♔': 'K'}

        self.binary = {"a":0,"b":1,"c":2,"d":3, "e":4, "f":5, "g":6, "h":7}
        self.binary_reversed = {7: 'h', 6: 'g', 5: 'f', 4: 'e', 3: 'd', 2: 'c', 1: 'b', 0: 'a'}

        self.master = master
        self.move_start=None
        self.piece_type = piece_type
        self.game_type = game_type
        self.move_stored = False
    
        self.border_width =border_width
        self.recent_moves = Stack.Stack()
        self.captured_pieces = Stack.Stack()
        {self.recent_moves.push(int(i)) for i in stack}

        white = colour_scheme[0]
        black =colour_scheme[1]
        self.colour_scheme = {"white": white, "black": black}

        self.piece_list = []
        self.white_pieces = []
        self.black_pieces = []   
        self.white_positions= xmpz(0)
        self.black_positions= xmpz(0) 
        self.black_king = None
        self.white_king = None   

        self.move_handler = Move_handler.Move_handler(self)
        self.old_passant = xmpz(0)

        
        self.ascii_board = np.zeros((8,8),dtype=str)
        self.FEN_extractor(FEN)
        self.board_background()
        self.create_boarder()
        self.create_backbutton()

        self.create_widgets()

        self.board  = np.array([[self.grid_slaves()[-(65+(8*a+i))] for i in range(8)] for a in range(8)])
        self.set_all_piece_moves()
        
        self.update_can_take("w")
        self.update_can_take("b")
        self.white_king.update_legal_moves()
        self.black_king.update_legal_moves()

                
    def __str__(self): 
        return f"{self.convert_into_fen()}"
    
    def destroy(self):
        super().destroy() 
        try:
            self.master.update_board.delete("1.0", tk.END)
            self.master.update_board.insert(tk.END, self.convert_into_fen(),self.recent_moves)
        except:
            return self.convert_into_fen(),self.recent_moves

        #return self.convert_into_fen(),self.recent_moves

        
    def create_widgets(self):
        for row in range(8):
            for col in range(8):
                temp = self.ascii_board[row][col]
                if temp == '':
                    piece = pieces.Piece(self,temp,row,col,self.piece_type)
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
                        self.white_positions[(row<<3)+col] = 1
                    else:
                        self.black_pieces = np.append(self.black_pieces,piece)
                        self.black_positions[(row<<3)+col] = 1

                    self.piece_list = np.append(self.piece_list,piece)
                                                                             
                piece.grid(row=row, column=col)
                self.move_handler.add_dragable(piece)
    
    def set_all_piece_moves(self):
        for i in self.piece_list:
            if i.ascii.lower() != "k":
                i.update_legal_moves()
        
    def create_boarder(self):
        side_border = tk.Frame(self,bg=self.colour_scheme["black"],height=(800),width=self.border_width)
        bottom_border = tk.Frame(self,bg=self.colour_scheme["black"],width=(800),height=self.border_width)

        for i in range(1,9):
            tk.Label(side_border,text=str(9-i), font = ("arial",15),fg=self.colour_scheme["white"],bg=self.colour_scheme["black"],pady=34).grid(column=0,row=(i-1),sticky="nesw")
            tk.Label(bottom_border,text=self.binary_reversed[i-1], font = ("arial",15),fg=self.colour_scheme["white"],bg=self.colour_scheme["black"],padx=42).grid(column=(i-1),row=0,sticky="nesw")
        bottom_border.place(rely =((800+1.5*self.border_width)/(800+2*self.border_width)), relx = 0.5,anchor="center", bordermode="ignore")
        side_border.place(relx =((0.5*self.border_width)/(800+2*self.border_width)), rely = 0.5,anchor="center", bordermode="ignore")
        
    def create_backbutton(self): #symbol is just a placeholder
        tk.Button(self, text="⬅️",font =("arial",13),fg = self.colour_scheme["white"],bg = self.colour_scheme["black"],borderwidth=0, command=self.reverse_move).place(relx =0, rely =1,anchor="sw", bordermode="ignore")

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
        column = 72340172838076673 # the numerical reprisentation of 1s down the left column of a 8x8 bitboard
        if colour == "b":
            self.black_can_take = xmpz(0)
            for i in self.black_pieces:
                if i.ascii == "p":
                    self.black_can_take |= (((column << (int(math.log2(i.pos))%8)) ^ ((2**64)-1)) & i.ghost_moves) # makes a mask with 0s int the column where the pawn is in order to make sure non capture moves arents added
                else:
                    self.black_can_take |= i.ghost_moves
                # elif i.ascii !="k":
                #     self.black_can_take |= i.ghost_moves
        else:
            self.white_can_take = xmpz(0)
            for i in self.white_pieces:
                if i.ascii == "P":
                    self.white_can_take |= (((column << (int(math.log2(i.pos))%8)) ^ ((2**64)-1)) & i.ghost_moves)
                else:
                    self.white_can_take |= i.ghost_moves
    #converts the move into a unique integer that is added to the stack so it can be reversed at any time
    def store_move(self,start,end,piece,type="quiet",captured="-"):
        if not self.move_stored:
            convert = {"p":1,"n":2,"b":3,"r":5,"q":6,"k":4,"P":9,"N":10,"B":11,"R":13,"Q":14,"K":12, "-":0}
            move_types = {'quiet': 0, 'double': 1, 'pawn': 1, 'push': 1, 'king-side': 2, 'queen-side': 3, 'capture': 4, 'ep-capture': 5, 'n-promo': 8, 'b-promo': 9, 'r-promo': 10, 'q-promo': 11, 'n-promo-capture': 12, 'b-promo-capture': 13, 'r-promo-capture': 14, 'q-promo-capture': 15}
            move =(convert[captured] << 20) + (convert[piece] <<16)+(((start[0]*8) + start[1]) <<10)+(((end[0]*8) + end[1]<<4)) +move_types[type]
            self.recent_moves.push(int(move)) # this is very ugly should be fixed
            self.move_stored = True
            
            #print(self.recent_moves.peak())
            #print(self.recent_moves)
    
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
            
            
            if "promo" in breakdown[-1]:
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
                self.replace_piece("",tk.Label(self),[erow,ecol],[srow,scol])
            else:
                if breakdown[0] == "ep-capture":
                    pass
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
            self.move_handler.update_affected_pieces(2**(erow*8+ecol),2**(srow*8+scol))
        
    def FEN_extractor(self,fen):
        fen = fen.split(" ")
        self.make_array_of_pieces(fen[0])
        self.active_colour = fen[1]
        self.avaiable_castle = fen[2]
        self.en_passant = xmpz(self.convert_from_binary(fen[3]))
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
        
        return f"{board} {self.active_colour} {self.avaiable_castle} {self.convert_to_binary(self.en_passant)} {self.half_move} {self.full_move}"
    
    def convert_from_binary(self,move):
        if move == '-':
            return 0
        return 2**((int(move[1])-1)*8+ self.binary[move[0]])
    
    def convert_to_binary(self,move):
        if (move == np.array([200,100])).any():
            return "-"
        return self.binary_reversed[move[1]] + str(8-move[0])
        
    
    
    
    
# once a pawn has reached the last rank it is deleted and the user is offered 4 options between for which piece they would like to promote to 
    def promote(self,piece,start,move_type=None,captured="-"):
        self.move_stored = True
        self.half_move += 1
        square = int(math.log2(piece.pos))
        row,col = square//8,square%8
        container = tk.Frame(self,width=100,height=100, bg="white" if (row+col)%2==0 else "gray", borderwidth=0,padx=0,pady=0)
        container.grid_columnconfigure(col, minsize=2)
        container.grid_rowconfigure(row, minsize=2)

        container.grid(row=row,column=col)
        self.captured_pieces.push(piece)
        piece.grid_remove()
        
        # tk.Button(container, bg= self.colour_scheme["white"], text="♛", font=["arial",15], command= lambda:[self.store_move(start,[row,col],piece.ascii,"q-"+move_type,captured),self.replace_piece("q",container,start,[row,col])]).grid(row=0,column=0, sticky= "nesw")
        # tk.Button(container, bg= self.colour_scheme["black"], text="♜" ,font=["arial",15], command= lambda:[ self.replace_piece("r",container,start,[row,col]), self.store_move(start,[row,col],piece.ascii,"r-"+move_type,captured)]).grid(row=0,column=1, sticky= "nesw")
        # tk.Button(container, bg= self.colour_scheme["black"], text="♝", font=["arial",15], command= lambda:[ self.replace_piece("b",container,start,[row,col]), self.store_move(start,[row,col],piece.ascii,"b-"+move_type,captured)]).grid(row=1,column=0, sticky= "nesw")
        # tk.Button(container, bg= self.colour_scheme["white"], text="♞", font=["arial",15], command= lambda:[ self.replace_piece("n",container,start,[row,col]), self.store_move(start,[row,col],piece.ascii,"n-"+move_type,captured)]).grid(row=1,column=1, sticky= "nesw")

        self.active_colour = None
        
        self.store_move(start,[row,col],piece.ascii,"q-"+move_type,captured)
        self.replace_piece("q",container,start,[row,col])

        # places a piece in the position of the pawn and corrects all the data structures to refelct this


    def replace_piece(self,p,container,start,pos):
        
        self.move_stored = False # essential as otherwise the program runs too fast in the drag handler and treats it as just a normal capture
        
        row,col = pos
        ssquare = 1<<(start[0]<<3+start[1])
        esquare = 1<<(row<<3+col)
        if self.half_move %2 ==1:
            piece_ascii = p.upper()
        else:
            piece_ascii = p

        if p == "p":
            piece = Pawn.Pawn(self,piece_ascii,row,col,self.piece_type)
        elif p == "":
            piece = pieces.Piece(self,'',row,col,piece_type='')
        elif p == "q":
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
        self.move_handler.add_dragable(piece)

        container.destroy()
        self.move_handler.update_affected_pieces(ssquare,esquare)

        self.active_colour = "w" if self.half_move %2 ==0 else "b"
        
        if self.half_move % 2 == 1:
            self.active_colour = "b"
            if self.white_king.pos & self.black_can_take:
                self.reverse_move()
        else:
            self.active_colour ="w"
            self.full_move += 1
            if self.black_king.pos & self.white_can_take:
                self.reverse_move()  
 

    def bot_make_move(self,start = 0,end = 0):
        if self.half_move % 2 == 0: 
            piece = self.white_pieces[random.randint(0,len(self.white_pieces)-1)]
            while not piece.legal_moves:
                piece = self.white_pieces[random.randint(0,len(self.white_pieces)-1)]
        else:
            piece = self.black_pieces[random.randint(0,len(self.black_pieces)-1)]
            while not piece.legal_moves:
                piece = self.black_pieces[random.randint(0,len(self.black_pieces)-1)]
        start = int(math.log2(piece.pos))
        temp = 0
        while not piece.legal_moves & temp:
            end = random.randint(0,64)
            temp = xmpz(0)
            temp[end] = 1
            
        self.move_handler.start_row,self.move_handler.start_col =start//8,start%8
        self.move_handler.on_drop("",False,end)
    

    def make_random_moves(self,depth=1):
        while depth >0:
            self.bot_make_move()
            depth-=1
            time.sleep(0.3)
            self.update()
