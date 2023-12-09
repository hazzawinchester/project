import numpy as np

class Stack:
  def __init__(self):
    self.data = np.array([],str)

  def __str__(self):
    return f"{self.data}"

  def push(self,item):
    self.item = np.append(self.item,item,axis =0)
    
  def pop(self):
    if not self.is_empty():
      out = self.data[-1]
      self.data = self.data[:-1]
      return out
    print("the stack is empty")
    
  def is_empty(self):
    return self.data == []

