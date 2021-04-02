""" 
 @author   Maksim Penkin
"""

import tkinter as tk
import random

LABEL_ACTIVE_COLOR = 'light grey'
LABEL_INACTIVE_COLOR = 'gray'
CURSOR_COLOR = 'gray22'
WIDTH_CHAR_PIX = 5

class Application(tk.Frame):
    """
        Base class for creating App
    """
    def __init__(self, master=None, title='Simple App', **kwargs):
        super().__init__(master, **kwargs)        
        self.master.title(title)
        self.master.rowconfigure(0, weight=1)
        self.master.columnconfigure(0, weight=1)
        for i in range(2):
            self.rowconfigure(i, weight=1)
        for j in range(1):
            self.columnconfigure(j, weight=1)
        self.grid(sticky="NEWS")
        self.createWidgets()

    def createWidgets(self):
        raise NotImplementedError

class CustomCursor(tk.Frame):
    def __init__(self, parent, height=15, width=1, bg=CURSOR_COLOR, **kwargs):
        super().__init__(parent, height=height, width=width, bg=bg, **kwargs) 
        self.pos = 0
        self.place(x=5)
        
    def set_position(self, p):
        self.place_forget()
        self.pos = p
        self.place(x=self.pos)
        return 

class CustomTextDisplay:
    def __init__(self, text='<some text>'):
        self.text = text 

    def __str__(self):
        return str(self.text)

    def __len__(self):
        return len(self.text)

class App(Application):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs) 

    def createWidgets(self):
        self.s = CustomTextDisplay()

        self.quit_Button = tk.Button(self, text='Quit', command=self.master.quit)
        self.mylabel = tk.Label(self, text=str(self.s),
                                takefocus=True,
                                borderwidth=2, relief="flat", background=LABEL_INACTIVE_COLOR,
                                justify='left', anchor='w', font="fixed")
        self.cursor = CustomCursor(self.mylabel, height=15, width=1, bg=CURSOR_COLOR)
        self.cursor.set_position(1)
        self.focus_set()
        self.cursor.focus_set()
        
        self.quit_Button.grid(row=1, column=0)
        self.mylabel.grid(row=0, column=0, sticky="EW")

        self.mylabel.bind("<Button-1>", lambda e: self.mouse_click_label(e))
        self.bind("<Button-1>", lambda e: self.mouse_click_out_label())
        self.bind_all("<Left>", lambda e: self.move_left())
        self.bind_all("<Right>", lambda e: self.move_right())
        self.bind_all("<Home>", lambda e: self.move_home())
        self.bind_all("<End>", lambda e: self.move_end())

    def mouse_click_label(self, e):
        self.mylabel.config(relief="sunken", background=LABEL_ACTIVE_COLOR)
        cursor_pos_new = min(((e.x // WIDTH_CHAR_PIX) * WIDTH_CHAR_PIX), len(self.s) * WIDTH_CHAR_PIX)
        self.cursor.set_position(cursor_pos_new)

    def mouse_click_out_label(self):
        self.cursor.set_position(1)
        self.mylabel.config(background=LABEL_INACTIVE_COLOR, relief="flat")

    def move_left(self):
        self.mylabel.config(relief="sunken", background=LABEL_ACTIVE_COLOR)
        cursor_pos_new = max(self.cursor.pos - WIDTH_CHAR_PIX, 0)
        self.cursor.set_position(cursor_pos_new)

    def move_right(self):
        self.mylabel.config(relief="sunken", background=LABEL_ACTIVE_COLOR)
        cursor_pos_new = min(self.cursor.pos + WIDTH_CHAR_PIX, len(self.s) * WIDTH_CHAR_PIX)
        self.cursor.set_position(cursor_pos_new)

    def move_home(self):
        self.mylabel.config(relief="sunken", background=LABEL_ACTIVE_COLOR)
        self.cursor.set_position(1)

    def move_end(self):
        self.mylabel.config(relief="sunken", background=LABEL_ACTIVE_COLOR)
        self.cursor.set_position(len(self.s) * WIDTH_CHAR_PIX)

if __name__ == "__main__":
    app = App()
    app.master.title('LabelEdit application')
    app.mainloop()
