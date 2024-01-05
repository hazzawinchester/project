from gmpy2 import xmpz
import numpy as np
import time

a=xmpz(7)

# king is at 7
#rook at 63
print(~7)


pos = 63
s = time.time()
for i in range(1):    
    rook = xmpz(sum([2**(i) for i in range(63%8+1)]) | sum([2**(0+(8*i)) for i in range(8)]))
#print(time.time()-s)    
    
rook = bin(rook)[2:].zfill(64)[::-1]
a= np.array([rook[i*8:i*8+8] for i in range(8)])

#print(a)

king = xmpz(2**57)

#( rook & king) if rook & king else print("no")


