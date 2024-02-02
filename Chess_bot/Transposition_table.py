# structure for a transposition table (hash) used to store moves for iteritive deepening
import numpy as np
import time
import random

class Transpoisition():
    def __init__(self):
        s=time.time()
        self.size =2147483647
        self.data = np.zeros(2147483647) #  largest prime less than 2^31
        self.data_sneaky= {}

        self.set_masks()

    
    def set_masks(self): # xor all parts together
        self.white_kings =np.array([[random.randint(1,2**64-1) for i in range(8)]for i in range(8)])
        self.white_queens =np.array([[random.randint(1,2**64-1) for i in range(8)]for i in range(8)])
        self.white_rooks =np.array([[random.randint(1,2**64-1) for i in range(8)]for i in range(8)])
        self.white_bishops =np.array([[random.randint(1,2**64-1) for i in range(8)]for i in range(8)])
        self.white_knights =np.array([[random.randint(1,2**64-1) for i in range(8)]for i in range(8)])
        self.white_pawns =np.array(np.append(np.append([[0,0,0,0,0,0,0,0]],[[random.randint(1,2**64-1) for i in range(8)]for i in range(6)],axis=0),[[0,0,0,0,0,0,0,0]],axis=0))
        
        self.black_kings =np.array([[random.randint(1,2**64-1) for i in range(8)]for i in range(8)])
        self.black_queens =np.array([[random.randint(1,2**64-1) for i in range(8)]for i in range(8)])
        self.black_rooks =np.array([[random.randint(1,2**64-1) for i in range(8)]for i in range(8)])
        self.black_bishops =np.array([[random.randint(1,2**64-1) for i in range(8)]for i in range(8)])
        self.black_knights =np.array([[random.randint(1,2**64-1) for i in range(8)]for i in range(8)])
        self.black_pawns =np.array(np.append(np.append([[0,0,0,0,0,0,0,0]],[[random.randint(1,2**64-1) for i in range(8)]for i in range(6)],axis=0),[[0,0,0,0,0,0,0,0]],axis=0))
        
        self.blacks_move = random.randint(1,2**64-1)
        self.castling = np.array([random.randint(1,2**64-1) for i in range(4)])
        self.passant_files = np.array([random.randint(1,2**64-1) for i in range(8)])
    
    def initial_hash(self,board):
        #pawdwad
        pass
    
    def Hash(self,move):
        pass
        #hashes the data and returns a given index in the hash table
        
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
        
        
        
a = Transpoisition()
