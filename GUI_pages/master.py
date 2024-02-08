import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image

class Window(tk.Tk):
     
    def __init__(self, *args, **kwargs): 
        tk.Tk.__init__(self, *args, **kwargs)
        
        self.title("Chess")
        self.geometry("1000x900")
        #self.state("zoomed")
        self.grid_rowconfigure(0, weight = 1)
        self.grid_rowconfigure(1, weight = 60)
        self.grid_columnconfigure(0, weight = 1)
        self.grid_columnconfigure(1, weight = 40)
        
        self.user = None
        self.display_pfp()
        
        self.lastpage = []
        self.current_frame = "Home"
        
        self.navigator = tk.Frame(self,bg="gray")
        self.navigator.grid(row=1,column=0,sticky="nesw")
        self.frames = {}  
        
        #back button 
        tk.Button(self.navigator,text="⬅️", font = ("arial",20),bg = "gray", command = lambda : (self.show_frame(self.lastpage[-1]),self.lastpage.pop(-1) if len(self.lastpage) != 1 else None)).pack(fill="x",side="bottom")
        
        
  
    # to display the current frame passed as parameter
    def show_frame(self, name):
        frame = self.frames[name]
        self.current_frame = name
        frame.tkraise()
    
    # adds a frame to a dictionary which contains all frames and adds button to the navigation bar for this frame so they can be displayed later
    def add_frame(self,frame,name):
            self.frames[name] = frame 
            frame.grid(row=0,column=1,sticky = "nesw",rowspan=2)
            tk.Button(self.navigator, text = name, font = ("arial",10), bg= "Gray",activebackground="#5b5b5b", command = lambda :
                (self.lastpage.append(self.current_frame) if name != self.current_frame else None,self.show_frame(name))).pack(fill="x")
            
    def display_pfp(self):
        if self.user == None:
            tk.Label(self,borderwidth=0,text ="♞",font = ("arial",40),bg="#5b5b5b",pady=0).grid(row=0,column=0,pady=0,sticky="nesw")
        else:
            img = Image.open(f"Users/test/test.png")
            img = img.resize((75, 75))
            img = ImageTk.PhotoImage(img)
            tk.Label(self,borderwidth=0,image=img,bg="#5b5b5b").grid(row=0,column=0)