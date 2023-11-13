import tkinter as tk # tk alias used for ease


"""
establishing a main

root = tk.Tk()

root.geometry("800x500") # initial size of window
root.title("Chess Program") # title of whole root window

#pack/grid/place to organise                                list passed into font of 2 values type and size




lable = tk.Label(root, text="Welcome to the chess program", font=("Arial", 18)) #root is the parent of lable -> lable is contained within root
# the lable now exists but is not placed inside of the root window -> pack/grid/place are used to put it in
lable.pack(padx=20,pady=20)
"""



"""using pack
textbox = tk.Text(root, font=("Arial", 14) , height="4") # a text input box with variable height but can also be scrolled
textbox.pack(padx=20,pady=10,fill="both")

entry = tk.Entry(root) # a input box with height only on and no scrolling
entry.pack(pady=0)

button = tk.Button(root, text=("click me")) #button that can be linked to functions
button.pack(pady=30)
"""


""" using grid


buttonframe = tk.Frame(root)
buttonframe.columnconfigure(0, weight=1)
buttonframe.columnconfigure(1, weight=1)
buttonframe.columnconfigure(2, weight=1)
buttonframe.columnconfigure(3, weight=1)
buttonframe.columnconfigure(4, weight=1)

btn1 = tk.Button(buttonframe, text="1")
btn1.grid(row=0, column=0, sticky="we") #creates a grid from the buttons above, sticky sticks the outsides of the grid to north east soth or west (hence "we" for west and east)
btn2 = tk.Button(buttonframe, text="2")
btn2.grid(row=0, column=1, sticky='we')
btn3 = tk.Button(buttonframe, text="3")
btn3.grid(row=0, column=2, sticky='we')
btn4 = tk.Button(buttonframe, text="4")
btn4.grid(row=0, column=3, sticky='we')
btn5 = tk.Button(buttonframe, text="5")
btn5.grid(row=0, column=4, sticky='we')

buttonframe.pack(fill="x")

"""


"""using place

butt = tk.Button(root, text="placed here using place")
butt.place(relx=.5, rely=.75, anchor="center", height=100,width=100) # state relative position of widget so will adapt to changing sizeor can just state xand y coordinates for it to be in (not good)
"""
"""root.mainloop()"""

from tkinter import messagebox
class mygui:
    def __init__(self):
        self.root = tk.Tk()

        self.lable = tk.Label(self.root, text="hi")
        self.lable.pack(side="bottom")

        self.textbox = tk.Text(self.root, height=5)
        self.textbox.bind("<KeyPress>",self.shortcut)
        self.textbox.pack(padx=10, pady=10)

        self.check_state = tk.IntVar()
        self.check = tk.Checkbutton(self.root, text="show Messagebox", variable=self.check_state)
        self.check.pack()


        self.button = tk.Button(self.root, text="message", command=self.show_message)
        self.button.pack()

        self.root.protocol("WM_DELETE_WINDOW", self.onclosing)

        self.menu = tk.Menu(self.root)
        self.filemenu = tk.Menu(self.menu, tearoff=0)
        self.filemenu.add_command(label="Close", command=self.onclosing)
        self.filemenu.add_command(label="Close no question", command=exit)
        self.menu.add_cascade(menu=self.filemenu, label="File")
        self.root.config(menu=self.menu)

        self.root.mainloop()

    def show_message(self):
        if self.check_state.get() == 0:
            print(self.textbox.get("1.0",tk.END))
        else:
            messagebox.showinfo(title="message", message=self.textbox.get("1.0",tk.END))

    def shortcut(self, event):
        if event.state == 4 and event.keysym == "Return": #state 4 means that ctrl is being held
            self.show_message()

    def onclosing(self):
        if messagebox.askyesno(title="Quit?", message="Do you want to quit"):
            self.root.destroy()
        

mygui()
