""" 
 @author   Maksim Penkin
"""

import tkinter as tk
from functools import partial


def constructWidget(master, name, widget_type, geometry, **kwargs):
    """
        Dynamic widget constructor 
    """
    class ChildWidget(widget_type):
        def __init__(self, geometry, **kwargs):
            super().__init__(**kwargs)

        def __getattr__(self, name):
            return partial(constructWidget, self, name)

    child_widget = ChildWidget(geometry, master=master, **kwargs)
    setattr(master, name, child_widget)
    return child_widget

class Application(tk.Frame):
    """
        Base class for creating App
    """
    def __init__(self, title):
        super().__init__(None)
        self.grid(sticky="NEWS")
        self.master.title(title)
        self.master.rowconfigure(0, weight=1)
        self.master.columnconfigure(0, weight=1)
        self.createWidgets()

    def __getattr__(self, name):
        return partial(constructWidget, self, name)

    def createWidgets(self):
        raise NotImplementedError

class App(Application):
    def createWidgets(self):
        self.message = "Congratulations!\nYou've found a sercet level!"
        self.F1(tk.LabelFrame, "1:0", text="Frame 1")
        self.F1.B1(tk.Button, "0:0/NW", text="1")
        self.F1.B2(tk.Button, "0:1/NE", text="2")
        self.F1.B3(tk.Button, "1:0+1/SEW", text="3")
        self.F2(tk.LabelFrame, "1:1", text="Frame 2")
        self.F2.B1(tk.Button, "0:0/N", text="4")
        self.F2.B2(tk.Button, "0+1:1/SEN", text="5")
        self.F2.B3(tk.Button, "1:0/S", text="6")
        self.Q(tk.Button, "2.0:1.2/SE", text="Quit", command=self.quit)
        self.F1.B3.bind("<Any-Key>", lambda event: showinfo(self.message.split()[0], self.message))

app = App(title="Sample application")
app.mainloop()


