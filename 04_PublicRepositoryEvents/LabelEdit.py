""" 
 @author   Maksim Penkin
"""

import tkinter as tk


class Application(tk.Frame):
    """
        Base class for creating App
    """
    def __init__(self, master=None, title='Simple App', **kwargs):
        super().__init__(master, **kwargs)        
        self.master.title(title)
        self.master.rowconfigure(0, weight=1)
        self.master.columnconfigure(0, weight=1)
        self.grid(sticky="NEWS")
        self.createWidgets()

    def createWidgets(self):
        raise NotImplementedError

class App(Application):
    def createWidgets(self):
        self.quit_Button = tk.Button(self, text='Quit', command=self.master.quit)
        self.quit_Button.grid()

if __name__ == "__main__":
    app = App()
    app.master.title('LabelEdit application')
    app.mainloop()