""" 
 @author   Maksim Penkin
"""

import tkinter as tk

class CustomText(tk.Text):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs) 

class CustomCanvas(tk.Frame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs) 
        self.master.rowconfigure(0, weight=1)
        self.master.columnconfigure(0, weight=1)
        for i in range(2):
            self.rowconfigure(i, weight=1)
        for j in range(1):
            self.columnconfigure(j, weight=1)
        self.grid(sticky="NEWS")
        self.createWidgets()

    def createWidgets(self):
        self.canvas = tk.Canvas(self)
        self.cursor_info_label = tk.Label(self, text='x: 0; y: 0', background='gray79')

        self.cursor_info_label.grid(row=0, column=0, sticky="NEWS")
        self.canvas.grid(row=1, column=0, sticky="NEWS") 

        self.canvas.bind("<Button-1>", self.on_mouse_left_push)
        self.canvas.bind("<ButtonRelease-1>", self.on_mouse_left_release)
        self.canvas.bind("<Motion>", self.on_mouse_move)

    def on_mouse_left_push(self, e):
        print(e.x, e.y)

    def on_mouse_left_release(self, e):
        print('RELEASED') 

    def on_mouse_move(self, e):
        self.cursor_info_label.config(text='x: {}; y: {}'.format(e.x, e.y))

class Application(tk.Frame):
    """
        Base class for creating App
    """
    def __init__(self, master=None, title='Simple App', **kwargs):
        super().__init__(master, **kwargs)        
        self.master.title(title)
        self.master.rowconfigure(0, weight=1)
        self.master.columnconfigure(0, weight=1)
        for i in range(4):
            self.rowconfigure(i, weight=1)
        for j in range(2):
            self.columnconfigure(j, weight=1)
        self.grid(sticky="NEWS")
        self.createWidgets()

    def createWidgets(self):
        raise NotImplementedError

class App(Application):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs) 

    def createWidgets(self):
        self.quit_Button = tk.Button(self, text='Quit', command=self.master.quit)
        self.update_txt_Button = tk.Button(self, text='Update TXT', command=None)
        self.update_canvas_Button = tk.Button(self, text='Update Canvas', command=None)

        self.label1 = tk.Label(self, text='TXT field', background='SkyBlue1')
        self.label2 = tk.Label(self, text='Canvas field', background='pink1')
        self.text = CustomText(self, undo=True, font="fixed", inactiveselectbackground="MidnightBlue")
        self.canvas = CustomCanvas(self)

        self.quit_Button.grid(row=0, column=0, sticky='NSEW')
        self.update_txt_Button.grid(row=1, column=0, sticky='NSEW')
        self.update_canvas_Button.grid(row=1, column=1, sticky='NSEW')
        self.label1.grid(row=2, column=0, sticky='NSEW')
        self.label2.grid(row=2, column=1, sticky='NSEW')
        self.text.grid(row=3, column=0, sticky='NSEW')
        self.canvas.grid(row=3, column=1, sticky='NSEW')

if __name__ == "__main__":
    app = App()
    app.master.title('05_SshAndSmartWidgents application')
    app.mainloop()


