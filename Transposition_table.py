# structure for a transposition table (hash) used to store moves for iteritive deepening
import numpy as np
import time

class Transpoisition():
    def __init__(self):
        s=time.time()
        self.data = np.zeros(2**32)
        print(time.time()-s)
    
    def Hash(self,data):
        pass
        #hashes the data and returns a given index in the hash table
        
    def insert(self,board):
        index = self.Hash(board)
        if not self.data[index]:
            self.data[index] = board
        #inserts data at a give index
        #need to figure out the best way to deal with colisions
        
    def find(self,index):
        pass
        # returns the data at a given index by hashing it and going to that index
        
        
        
a = Transpoisition()
