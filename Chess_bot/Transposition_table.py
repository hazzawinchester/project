# structure for a transposition table (hash) used to store moves for iteritive deepening
from Chess_bot import rn
import numpy as np
import time

class Transpoisition():
    def __init__(self,master):
        s=time.time()
        self.master = master
        self.size =2147483647
        #self.data = np.zeros(2147483647) #  largest prime less than 2^31
        self.data_sneaky= {}
        self.random_context = rn.Ranctx()
        
        self.prev_passant = 0

        self.set_masks()

    def generate_random_number(self):
        self.total += 281 # random prime for less congruent keys
        rn.raninit(self.random_context, self.total)
        return int(rn.ranval(self.random_context) & 0xFFFFFFFFFFFFFFFF)
    
    def set_masks(self): # xor all parts together
        self.total = 0
        self.white_kings =np.array([[self.generate_random_number() for a in range(8)]for b in range(8)])
        self.white_queens =np.array([[self.generate_random_number() for a in range(8)]for b in range(8)])
        self.white_rooks =np.array([[self.generate_random_number() for a in range(8)]for b in range(8)])
        self.white_bishops =np.array([[self.generate_random_number() for a in range(8)]for b in range(8)])
        self.white_knights =np.array([[self.generate_random_number() for a in range(8)]for b in range(8)])
        self.white_pawns =np.array(np.append(np.append([[0,0,0,0,0,0,0,0]],[[self.generate_random_number() for a in range(8)]for b in range(6)],axis=0),[[0,0,0,0,0,0,0,0]],axis=0))
        
        self.black_kings =np.array([[self.generate_random_number() for a in range(8)]for b in range(8)])
        self.black_queens =np.array([[self.generate_random_number() for a in range(8)]for b in range(8)])
        self.black_rooks =np.array([[self.generate_random_number() for a in range(8)]for b in range(8)])
        self.black_bishops =np.array([[self.generate_random_number() for a in range(8)]for b in range(8)])
        self.black_knights =np.array([[self.generate_random_number() for a in range(8)]for b in range(8)])
        self.black_pawns =np.array(np.append(np.append([[0,0,0,0,0,0,0,0]],[[self.generate_random_number() for a in range(8)]for b in range(6)],axis=0),[[0,0,0,0,0,0,0,0]],axis=0))
        
        self.white_hash = np.array([self.white_pawns,self.white_knights,self.white_bishops,self.white_rooks,self.white_queens,self.white_kings])
        self.black_hash = np.array([self.black_pawns,self.black_knights,self.black_bishops,self.black_rooks,self.black_queens,self.black_kings])
        
        self.blacks_move = self.generate_random_number()
        self.castling = np.array([self.generate_random_number() for i in range(4)])
        self.passant_files = np.array([self.generate_random_number() for i in range(8)])
        
    
    def initial_hash(self,board):
        hash = 0
        white,black = board
        for i in range(6):
            a= white[i].bit_scan1(0)
            while a != None:
                hash ^= int(self.white_hash[i][a//8,a%8])
                a= white[i].bit_scan1(a+1)

            b= black[i].bit_scan1(0)
            while b != None:
                hash ^= int(self.black_hash[i][b//8,b%8])
                b= black[i].bit_scan1(b+1)
        
        b= self.master.available_castle.bit_scan1(0)
        while b != None:
            hash ^=  int(self.castling[b])
            b = self.master.available_castle.bit_scan1(b+1)
            
        return hash
        
    def hash(self,move,hash):
        hash ^= self.blacks_move ^ self.prev_passant
        
        
        out = str(bin(move)[2:].zfill(24))
        captured,piece,start,end,type = [int(out[:4],2), int(out[4:8],2), [(int(out[8:11],2)),(int(out[11:14],2))], [(int(out[14:17],2)),(int(out[17:20],2))], int(out[20:],2)]
        
        if captured:
            if captured >7:
                hash ^= int(self.white_hash[captured%8-1][end[0],end[1]])
            else:
                hash ^= int(self.black_hash[captured-1][end[0],end[1]])
        
        if piece >7:
            hash ^= int(self.white_hash[piece%8-1][start[0],start[1]]) ^ int(self.white_hash[piece%8-1][end[0],end[1]])
        else:
            hash ^= int(self.black_hash[piece-1][start[0],start[1]]) ^ int(self.black_hash[piece%8-1][end[0],end[1]])
            
        return hash
        #hashes the data and returns a given index in the hash table
        
    def undo_castling(self,hash,index):
        pass
        
    def insert(self,board):
        index = self.Hash(board)
        if not self.data[index]:
            self.data[index] = board
        #inserts data at a give index
        #need to figure out the best way to deal with colisions
        
    def find(self,data):
        return self.data[self.hash(data)]
        pass
        # returns the data at a given index by hashing it and going to that index
