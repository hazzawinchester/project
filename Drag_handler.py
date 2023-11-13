import tkinter as tk

class Drag_handler():
    def add_dragable(self, widget):
        widget.bind("<ButtonPress-1>", self.on_start)
        widget.bind("<B1-Motion>", self.on_drag)
        widget.bind("<ButtonRelease-1>", self.on_drop)

    def on_start(self, event):
        # you could use this method to create a floating window
        # that represents what is being dragged.
        # print(event.x,event.y)
        self.start_x,self.start_y = (event.y_root-event.widget.master.winfo_rooty())//100,(event.x_root-event.widget.master.winfo_rootx())//100
        pass

    def on_drag(self, event):
        #x,y = event.widget.winfo_pointerxy()
        event.widget.place(x=(event.x_root-event.widget.master.winfo_rootx()),y=(event.y_root-event.widget.master.winfo_rooty()),anchor="center")
        pass

    def on_drop(self, event):
        # find the widget under the cursor
        x,y = (event.y_root-event.widget.master.winfo_rooty())//100,(event.x_root-event.widget.master.winfo_rootx())//100
        if x != self.start_x or y!= self.start_y:
            event.widget.master.grid_slaves(x,y)[0].destroy()
            event.widget.grid(row=x,column=y)

            temp =tk.Label(event.widget.master,text='', font=("Arial",50), borderwidth=0)
            temp.grid(row=self.start_x,column=self.start_y)
        else:
            event.widget.grid(row=self.start_x,column=self.start_y)
