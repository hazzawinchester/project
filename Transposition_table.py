# structure for a transposition table (hash) used to store moves for iteritive deepening
import numpy as np

class Transpoisition():
    def __init__(self):
        self.data = np.array(100)
    
    def Hash(self,data):
        pass
        #hashes the data and returns a given index in the hash table
        
    def insert(self,index,data):
        pass
        #inserts data at a give index
        #need to figure out the best way to deal with colisions
        
    def find(self,index):
        pass
        # returns the data at a given index by hashing it and going to that index
        
        

print("FUCK ME ")