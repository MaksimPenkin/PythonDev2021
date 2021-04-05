""" 
 @author   Maksim Penkin
"""

import tkinter as tk


OVAL_COLOR = 'VioletRed1'
OVAL_BORDER_COLOR = 'dark orchid'
OVAL_BORDER_WIDTH = 2
MIN_RAD = 10
EPS_OVERLAP = 3

class Oval:
    def __init__(self, x0, y0, x1, y1, fill_color=OVAL_COLOR, outline_color=OVAL_BORDER_COLOR, width=OVAL_BORDER_WIDTH):
        self.x0 = int(x0)
        self.y0 = int(y0)

        self.x1 = int(x1)
        self.y1 = int(y1)

        self.fill_color = fill_color
        self.outline_color = outline_color
        self.width = width

    def get_tk_coords(self):
        return (self.x0, self.y0, self.x1, self.y1)

    def update(self, delta_x, delta_y):
        self.x0 = int(self.x0 + delta_x)
        self.y0 = int(self.y0 + delta_y)

        self.x1 = int(self.x1 + delta_x)
        self.y1 = int(self.y1 + delta_y)

class CustomText(tk.Text):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs) 

    def clear(self):
        self.delete("1.0", tk.END)

    def update_info(self, str_in):
        self.clear()
        self.insert("1.0", str_in)

class CustomCanvas(tk.Frame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs) 
        self.ovals = dict()
        self.pushed = None

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
        found_overlaps = self.canvas.find_overlapping(e.x-EPS_OVERLAP, e.y-EPS_OVERLAP, e.x+EPS_OVERLAP, e.y+EPS_OVERLAP)
        if found_overlaps:
            self.pushed = found_overlaps[-1]
        else:
            oval = Oval(e.x - MIN_RAD, e.y - MIN_RAD, e.x + MIN_RAD, e.y + MIN_RAD,
                        fill_color=OVAL_COLOR, outline_color=OVAL_BORDER_COLOR, width=OVAL_BORDER_WIDTH)
            oval_id = self.canvas.create_oval(oval.x0, oval.y0, oval.x1, oval.y1,
                                              fill=oval.fill_color, outline=oval.outline_color, width=oval.width)
            self.ovals[oval_id] = oval

    def on_mouse_left_release(self, e):
        self.pushed = None

    def on_mouse_move(self, e):
        self.cursor_info_label.config(text='x: {}; y: {}'.format(e.x, e.y))
        if self.pushed:
            x0, y0, x1, y1 = self.ovals[self.pushed].get_tk_coords()
            x_center = (x0 + x1) / 2.0
            y_center = (y0 + y1) / 2.0
            delta_x, delta_y = e.x - x_center, e.y - y_center
            self.canvas.coords(self.pushed, int(x0+delta_x), int(y0+delta_y), int(x1+delta_x), int(y1+delta_y))
            self.ovals[self.pushed].update(delta_x, delta_y)

    def destroyWidgets(self):
        self.canvas.grid_forget()
        self.cursor_info_label.grid_forget()

    def clear(self):
        self.canvas.delete("all")
        self.ovals = dict()
        self.pushed = None
        self.destroyWidgets()
        self.createWidgets()

    def update_info(self, ovals_in):
        self.clear()
        for _, oval in ovals_in.items():
            oval_id = self.canvas.create_oval(oval.x0, oval.y0, oval.x1, oval.y1,
                                              fill=oval.fill_color, outline=oval.outline_color, width=oval.width)
            self.ovals[oval_id] = oval

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
        self.update_txt_Button = tk.Button(self, text='Update TXT', command=self.update_txt_handler)
        self.update_canvas_Button = tk.Button(self, text='Update Canvas', command=self.update_canvas_handler)
        self.clear_Button = tk.Button(self, text='Clear', command=self.clear)

        self.label1 = tk.Label(self, text='TXT field', background='SkyBlue1')
        self.label2 = tk.Label(self, text='Canvas field', background='pink1')
        
        self.text = CustomText(self, undo=True, font="fixed")
        self.canvas = CustomCanvas(self)

        self.quit_Button.grid(row=0, column=0, sticky='NSEW')
        self.clear_Button.grid(row=0, column=1, sticky='NSEW')
        self.update_txt_Button.grid(row=1, column=0, sticky='NSEW')
        self.update_canvas_Button.grid(row=1, column=1, sticky='NSEW')
        self.label1.grid(row=2, column=0, sticky='NSEW')
        self.label2.grid(row=2, column=1, sticky='NSEW')
        self.text.grid(row=3, column=0, sticky='NSEW')
        self.canvas.grid(row=3, column=1, sticky='NSEW')

    def update_txt_handler(self):
        # Each oval is encoded as: ID;X0;Y0;X1;Y1;WIDTH;IN_COLOR;BORDER_COLOR
        str_out = ""
        for oval_id, oval in self.canvas.ovals.items():
            x0, y0, x1, y1 = oval.get_tk_coords()
            w = oval.width
            f = oval.fill_color
            b = oval.outline_color
            str_out += str(oval_id) + ';' + ';'.join([str(x0), str(y0), str(x1), str(y1)]) + ';' + str(w) + ';' + f + ';' + b + '\n'

        self.text.update_info(str_out)

    def unpackline(self, line):
        line_list = line.split(';')
        id_oval, x0, y0, x1, y1, w, f, b = line.split(';')
        
        return id_oval, x0, y0, x1, y1, w, f, b

    def update_canvas_handler(self):
        str_list = self.text.get("1.0", tk.END).split('\n')
        ovals_out = dict()
        for line in str_list:
            if line != '':
                id_oval, x0, y0, x1, y1, w, f, b = self.unpackline(line)
                ovals_out[id_oval] = Oval(x0, y0, x1, y1, fill_color=f, outline_color=b, width=w)

        self.canvas.update_info(ovals_out)

    def clear(self):
        self.text.clear()
        self.canvas.clear()

if __name__ == "__main__":
    app = App()
    app.master.title('05_SshAndSmartWidgents application')
    app.mainloop()


