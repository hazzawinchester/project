import tkinter as tk
import pieces as p

#drag handler adds the drag functionality to all pieces by giving them these the following methods
#this allows pieces to be added dynamicaly whenever needed
class Drag_handler():
    def add_dragable(self, widget):
        widget.bind("<ButtonPress-1>", self.on_start)
        widget.bind("<B1-Motion>", self.on_drag)
        widget.bind("<ButtonRelease-1>", self.on_drop)

    def on_start(self, event):
        #documents the starting point of the piece so it can be returned if the move is invalid
        self.start_x,self.start_y = (event.y_root-event.widget.master.winfo_rooty())//100,(event.x_root-event.widget.master.winfo_rootx())//100
        pass

    def on_drag(self, event):
        #makes the piece follow beneath the position of the mouse on the screen by redrawing every time it moves
        event.widget.place(x=(event.x_root-event.widget.master.winfo_rootx()),y=(event.y_root-event.widget.master.winfo_rooty()),anchor="center")
        event.widget.lift()
        pass

    def on_drop(self, event):
        #locks the widget into the nearst gird space or retruns it to the starting point if it is invalid
        x,y = (event.y_root-event.widget.master.winfo_rooty())//100,(event.x_root-event.widget.master.winfo_rootx())//100
        if (x != self.start_x or y!= self.start_y )and x<8 and y<8 and x>=0 and y>=0 and (event.widget.colour != event.widget.master.grid_slaves(x,y)[0].colour):
            event.widget.master.grid_slaves(x,y)[0].destroy()
            event.widget.grid(row=x,column=y)

            temp = p.Piece(event.widget.master,piece='',row=self.start_x,col=self.start_y,piece_type='')
            temp.grid(row=self.start_x,column=self.start_y)
        else:
            event.widget.grid(row=self.start_x,column=self.start_y)
