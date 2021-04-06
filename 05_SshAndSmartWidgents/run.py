""" 
 @author   Maksim Penkin
"""

import tkinter as tk


OVAL_COLOR = 'VioletRed1'
OVAL_BORDER_COLOR = 'dark orchid'
OVAL_BORDER_WIDTH = 2
MIN_RAD = 10
EPS_OVERLAP = 3

TKINTER_COLORS = ['snow', 'ghost white', 'white smoke', 'gainsboro', 'floral white', 'old lace',
'linen', 'antique white', 'papaya whip', 'blanched almond', 'bisque', 'peach puff',
'navajo white', 'lemon chiffon', 'mint cream', 'azure', 'alice blue', 'lavender',
'lavender blush', 'misty rose', 'dark slate gray', 'dim gray', 'slate gray',
'light slate gray', 'gray', 'light grey', 'midnight blue', 'navy', 'cornflower blue', 'dark slate blue',
'slate blue', 'medium slate blue', 'light slate blue', 'medium blue', 'royal blue',  'blue',
'dodger blue', 'deep sky blue', 'sky blue', 'light sky blue', 'steel blue', 'light steel blue',
'light blue', 'powder blue', 'pale turquoise', 'dark turquoise', 'medium turquoise', 'turquoise',
'cyan', 'light cyan', 'cadet blue', 'medium aquamarine', 'aquamarine', 'dark green', 'dark olive green',
'dark sea green', 'sea green', 'medium sea green', 'light sea green', 'pale green', 'spring green',
'lawn green', 'medium spring green', 'green yellow', 'lime green', 'yellow green',
'forest green', 'olive drab', 'dark khaki', 'khaki', 'pale goldenrod', 'light goldenrod yellow',
'light yellow', 'yellow', 'gold', 'light goldenrod', 'goldenrod', 'dark goldenrod', 'rosy brown',
'indian red', 'saddle brown', 'sandy brown',
'dark salmon', 'salmon', 'light salmon', 'orange', 'dark orange',
'coral', 'light coral', 'tomato', 'orange red', 'red', 'hot pink', 'deep pink', 'pink', 'light pink',
'pale violet red', 'maroon', 'medium violet red', 'violet red',
'medium orchid', 'dark orchid', 'dark violet', 'blue violet', 'purple', 'medium purple',
'thistle', 'snow2', 'snow3',
'snow4', 'seashell2', 'seashell3', 'seashell4', 'AntiqueWhite1', 'AntiqueWhite2',
'AntiqueWhite3', 'AntiqueWhite4', 'bisque2', 'bisque3', 'bisque4', 'PeachPuff2',
'PeachPuff3', 'PeachPuff4', 'NavajoWhite2', 'NavajoWhite3', 'NavajoWhite4',
'LemonChiffon2', 'LemonChiffon3', 'LemonChiffon4', 'cornsilk2', 'cornsilk3',
'cornsilk4', 'ivory2', 'ivory3', 'ivory4', 'honeydew2', 'honeydew3', 'honeydew4',
'LavenderBlush2', 'LavenderBlush3', 'LavenderBlush4', 'MistyRose2', 'MistyRose3',
'MistyRose4', 'azure2', 'azure3', 'azure4', 'SlateBlue1', 'SlateBlue2', 'SlateBlue3',
'SlateBlue4', 'RoyalBlue1', 'RoyalBlue2', 'RoyalBlue3', 'RoyalBlue4', 'blue2', 'blue4',
'DodgerBlue2', 'DodgerBlue3', 'DodgerBlue4', 'SteelBlue1', 'SteelBlue2',
'SteelBlue3', 'SteelBlue4', 'DeepSkyBlue2', 'DeepSkyBlue3', 'DeepSkyBlue4',
'SkyBlue1', 'SkyBlue2', 'SkyBlue3', 'SkyBlue4', 'LightSkyBlue1', 'LightSkyBlue2',
'LightSkyBlue3', 'LightSkyBlue4', 'SlateGray1', 'SlateGray2', 'SlateGray3',
'SlateGray4', 'LightSteelBlue1', 'LightSteelBlue2', 'LightSteelBlue3',
'LightSteelBlue4', 'LightBlue1', 'LightBlue2', 'LightBlue3', 'LightBlue4',
'LightCyan2', 'LightCyan3', 'LightCyan4', 'PaleTurquoise1', 'PaleTurquoise2',
'PaleTurquoise3', 'PaleTurquoise4', 'CadetBlue1', 'CadetBlue2', 'CadetBlue3',
'CadetBlue4', 'turquoise1', 'turquoise2', 'turquoise3', 'turquoise4', 'cyan2', 'cyan3',
'cyan4', 'DarkSlateGray1', 'DarkSlateGray2', 'DarkSlateGray3', 'DarkSlateGray4',
'aquamarine2', 'aquamarine4', 'DarkSeaGreen1', 'DarkSeaGreen2', 'DarkSeaGreen3',
'DarkSeaGreen4', 'SeaGreen1', 'SeaGreen2', 'SeaGreen3', 'PaleGreen1', 'PaleGreen2',
'PaleGreen3', 'PaleGreen4', 'SpringGreen2', 'SpringGreen3', 'SpringGreen4',
'green2', 'green3', 'green4', 'chartreuse2', 'chartreuse3', 'chartreuse4',
'OliveDrab1', 'OliveDrab2', 'OliveDrab4', 'DarkOliveGreen1', 'DarkOliveGreen2',
'DarkOliveGreen3', 'DarkOliveGreen4', 'khaki1', 'khaki2', 'khaki3', 'khaki4',
'LightGoldenrod1', 'LightGoldenrod2', 'LightGoldenrod3', 'LightGoldenrod4',
'LightYellow2', 'LightYellow3', 'LightYellow4', 'yellow2', 'yellow3', 'yellow4',
'gold2', 'gold3', 'gold4', 'goldenrod1', 'goldenrod2', 'goldenrod3', 'goldenrod4',
'DarkGoldenrod1', 'DarkGoldenrod2', 'DarkGoldenrod3', 'DarkGoldenrod4',
'RosyBrown1', 'RosyBrown2', 'RosyBrown3', 'RosyBrown4', 'IndianRed1', 'IndianRed2',
'IndianRed3', 'IndianRed4', 'sienna1', 'sienna2', 'sienna3', 'sienna4', 'burlywood1',
'burlywood2', 'burlywood3', 'burlywood4', 'wheat1', 'wheat2', 'wheat3', 'wheat4', 'tan1',
'tan2', 'tan4', 'chocolate1', 'chocolate2', 'chocolate3', 'firebrick1', 'firebrick2',
'firebrick3', 'firebrick4', 'brown1', 'brown2', 'brown3', 'brown4', 'salmon1', 'salmon2',
'salmon3', 'salmon4', 'LightSalmon2', 'LightSalmon3', 'LightSalmon4', 'orange2',
'orange3', 'orange4', 'DarkOrange1', 'DarkOrange2', 'DarkOrange3', 'DarkOrange4',
'coral1', 'coral2', 'coral3', 'coral4', 'tomato2', 'tomato3', 'tomato4', 'OrangeRed2',
'OrangeRed3', 'OrangeRed4', 'red2', 'red3', 'red4', 'DeepPink2', 'DeepPink3', 'DeepPink4',
'HotPink1', 'HotPink2', 'HotPink3', 'HotPink4', 'pink1', 'pink2', 'pink3', 'pink4',
'LightPink1', 'LightPink2', 'LightPink3', 'LightPink4', 'PaleVioletRed1',
'PaleVioletRed2', 'PaleVioletRed3', 'PaleVioletRed4', 'maroon1', 'maroon2',
'maroon3', 'maroon4', 'VioletRed1', 'VioletRed2', 'VioletRed3', 'VioletRed4',
'magenta2', 'magenta3', 'magenta4', 'orchid1', 'orchid2', 'orchid3', 'orchid4', 'plum1',
'plum2', 'plum3', 'plum4', 'MediumOrchid1', 'MediumOrchid2', 'MediumOrchid3',
'MediumOrchid4', 'DarkOrchid1', 'DarkOrchid2', 'DarkOrchid3', 'DarkOrchid4',
'purple1', 'purple2', 'purple3', 'purple4', 'MediumPurple1', 'MediumPurple2',
'MediumPurple3', 'MediumPurple4', 'thistle1', 'thistle2', 'thistle3', 'thistle4',
'gray1', 'gray2', 'gray3', 'gray4', 'gray5', 'gray6', 'gray7', 'gray8', 'gray9', 'gray10',
'gray11', 'gray12', 'gray13', 'gray14', 'gray15', 'gray16', 'gray17', 'gray18', 'gray19',
'gray20', 'gray21', 'gray22', 'gray23', 'gray24', 'gray25', 'gray26', 'gray27', 'gray28',
'gray29', 'gray30', 'gray31', 'gray32', 'gray33', 'gray34', 'gray35', 'gray36', 'gray37',
'gray38', 'gray39', 'gray40', 'gray42', 'gray43', 'gray44', 'gray45', 'gray46', 'gray47',
'gray48', 'gray49', 'gray50', 'gray51', 'gray52', 'gray53', 'gray54', 'gray55', 'gray56',
'gray57', 'gray58', 'gray59', 'gray60', 'gray61', 'gray62', 'gray63', 'gray64', 'gray65',
'gray66', 'gray67', 'gray68', 'gray69', 'gray70', 'gray71', 'gray72', 'gray73', 'gray74',
'gray75', 'gray76', 'gray77', 'gray78', 'gray79', 'gray80', 'gray81', 'gray82', 'gray83',
'gray84', 'gray85', 'gray86', 'gray87', 'gray88', 'gray89', 'gray90', 'gray91', 'gray92',
'gray93', 'gray94', 'gray95', 'gray97', 'gray98', 'gray99']

class Oval:
    def __init__(self, x0, y0, x1, y1, fill_color=OVAL_COLOR, border_color=OVAL_BORDER_COLOR, width=OVAL_BORDER_WIDTH):
        self.x0 = int(x0)
        self.y0 = int(y0)

        self.x1 = int(x1)
        self.y1 = int(y1)

        self.fill_color = fill_color
        self.border_color = border_color
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
                        fill_color=OVAL_COLOR, border_color=OVAL_BORDER_COLOR, width=OVAL_BORDER_WIDTH)
            oval_id = self.canvas.create_oval(oval.x0, oval.y0, oval.x1, oval.y1,
                                              fill=oval.fill_color, outline=oval.border_color, width=oval.width)
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
                                              fill=oval.fill_color, outline=oval.border_color, width=oval.width)
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

        self.add_tags()

    def add_tags(self):
        self.text.tag_config("E", background='red')
    
    def refresh_tags(self):
        for tag in self.text.tag_names():
            self.text.tag_delete(tag)
        self.add_tags()
    
    def update_txt_handler(self):
        self.refresh_tags()
        # Each oval is encoded as: ID;X0;Y0;X1;Y1;WIDTH;IN_COLOR;BORDER_COLOR
        str_out = ""
        for oval_id, oval in self.canvas.ovals.items():
            x0, y0, x1, y1 = oval.get_tk_coords()
            w = oval.width
            f = oval.fill_color
            b = oval.border_color
            str_out += str(oval_id) + ';' + ';'.join([str(x0), str(y0), str(x1), str(y1)]) + ';' + str(w) + ';' + f + ';' + b + '\n'

        self.text.update_info(str_out)

    def correctline(self, line):
        # Each oval is encoded as: ID;X0;Y0;X1;Y1;WIDTH;IN_COLOR;BORDER_COLOR
        line_split = line.split(';')
        if len(line_split) != 8:
            return False 
        id_oval, x0, y0, x1, y1, w, f, b = line_split
        try:
            id_oval = int(id_oval)
            x0 = float(x0)
            x1 = float(x1)
            y0 = float(y0)
            y1 = float(y1)
            w = float(w)
        except ValueError:
            return False 
        if (f not in TKINTER_COLORS) or (b not in TKINTER_COLORS):
            return False 
        
        return True
    
    def unpackline(self, line, idx_line):
        if not self.correctline(line):
            self.text.tag_add("E", f"{idx_line+1}.0", f"{idx_line+1}.end")
            return None
        else:
            line_list = line.split(';')
            id_oval, x0, y0, x1, y1, w, f, b = line.split(';')
            
            return id_oval, x0, y0, x1, y1, w, f, b

    def update_canvas_handler(self):
        self.refresh_tags()

        str_list = self.text.get("1.0", tk.END).split('\n')
        ovals_out = dict()
        for idx_line, line in enumerate(str_list):
            if line != '':
                st = self.unpackline(line, idx_line)
                if st is not None:
                    id_oval, x0, y0, x1, y1, w, f, b = st
                    ovals_out[id_oval] = Oval(x0, y0, x1, y1, fill_color=f, border_color=b, width=w)

        self.canvas.update_info(ovals_out)

    def clear(self):
        self.refresh_tags()
        self.text.clear()
        self.canvas.clear()

if __name__ == "__main__":
    app = App()
    app.master.title('05_SshAndSmartWidgents application')
    app.mainloop()


