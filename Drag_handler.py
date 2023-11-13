import tkinter as tk
class Drag_handler():
    def add_dragable(self, widget):
        widget.bind("<ButtonPress-1>", self.on_start)
        widget.bind("<B1-Motion>", self.on_drag)
        widget.bind("<ButtonRelease-1>", self.on_drop)

    def on_start(self, event):
        # you could use this method to create a floating window
        # that represents what is being dragged.
        print(event.x,event.y,event.widget.master.x)
        #print(event.x_root,event.y_root)
        print("CLICEKD")
        pass

    def on_drag(self, event,widget=None):
        #x,y = event.widget.winfo_pointerxy()
        x,y = event.x_root,event.y_root
        print(x,y)
        event.widget.place(x=x,y=y)
        pass

    def on_drop(self, event):
        # find the widget under the cursor
        x,y = event.widget.winfo_pointerxy()
        x,y = event.x,event.y
        target = event.widget.winfo_containing(x,y)
        try:
            target.configure(image=event.widget.cget("image"))
        except:
            pass
