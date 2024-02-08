import tkinter as tk

window = tk.Tk()

white = "white"
black = "Gray"
pieces = [["r","n","b","q","k","b","n","r"],["p","p","p","p","p","p","p","p"],['','','','','','','',''],['','','','','','','',''],['','','','','','','',''],['','','','','','','',''],["P","P","P","P","P","P","P","P"],["R","N","B","Q","K","B","N","R"]] #represent
for row in range(8):
    for col in range(8):
        squares = tk.Button(window, bg= white if (row+col)%2==0 else black, text= pieces[row][col], width=5,height=3 )
        squares.grid(row=row, column=col)
        

window.mainloop()