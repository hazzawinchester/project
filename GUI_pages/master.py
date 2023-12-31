import tkinter as tk
from tkinter import ttk
class Window(tk.Tk):
     
    def __init__(self, *args, **kwargs): 
        tk.Tk.__init__(self, *args, **kwargs)
        
        self.title("Chess")
        self.geometry("1000x1000")
        self.state("zoomed")
        self.grid_rowconfigure(0, weight = 1)
        self.grid_rowconfigure(1, weight = 60)
        self.grid_columnconfigure(0, weight = 1)
        self.grid_columnconfigure(1, weight = 40)
        
        self.user = None
        self.display_pfp()
        
        
        self.navigator = tk.Frame(self,bg="gray")
        self.navigator.grid(row=1,column=0,sticky="nesw")
        self.frames = {}  
  
    # to display the current frame passed as parameter
    def show_frame(self, name):
        frame = self.frames[name]
        frame.tkraise()
    
    def add_frame(self,frame,name):
            self.frames[name] = frame 
            frame.grid(row=0,column=1,sticky = "nesw",rowspan=2)
            ttk.Button(self.navigator,width=10, text = name, command = lambda : self.show_frame(name)).pack()
            
    def display_pfp(self):
        if self.user == None:
            tk.Label(self,borderwidth=0,text ="♞",font = ("arial",40),bg="#5b5b5b",pady=0).grid(row=0,column=0,pady=0,sticky="nesw")
        else:
            img = Image.open(f"Users/test/test.png")
            img = img.resize((75, 75))
            img = ImageTk.PhotoImage(img)
            tk.Label(self,borderwidth=0,image=img,bg="#6b6b6b").grid(row=0,column=0)