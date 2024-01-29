import multiprocessing as mp
import os
import time
from gmpy2 import xmpz


    
import tkinter as tk
from tkinter import messagebox, ttk

from tkinter import *

# Import module 
top = Tk()
CheckVar1 = IntVar()
CheckVar2 = IntVar()
C1 = Checkbutton(top, text = "Music", variable = CheckVar1, \
   onvalue = 1, offvalue = 0, height=5, \
   width = 20, )
C2 = Checkbutton(top, text = "Video", variable = CheckVar2, \
   onvalue = 1, offvalue = 0, height=5, \
   width = 20)
C1.pack()
C2.pack()
top.mainloop()