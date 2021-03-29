""" 
 @author   Maksim Penkin
"""

import tkinter as tk


class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid(sticky='NSEW')
        self.h = 4
        self.w = 4
        self.button_number = [[None]*self.w]*self.h
        
        # https://stackoverflow.com/questions/7591294/how-to-create-a-self-resizing-grid-of-buttons-in-tkinter/38809894
        root=self.winfo_toplevel()
        root.rowconfigure(0, weight=1)
        root.columnconfigure(0, weight=1)
        for i in range(self.h+1):
            self.rowconfigure(i, weight=1)
        for j in range(self.w):
            self.columnconfigure(j, weight=1)
        
        # New button
        self.button_new = tk.Button(master=self,
                                    text='New',
                                    activebackground='green yellow',
                                    bg='lime green',
                                    command=None)
        self.button_new.grid(row=0, column=0, columnspan=2, sticky='NS')

        # Quit button
        self.button_quit = tk.Button(master=self,
                                    text='Quit',
                                    activebackground='honeydew3',
                                    bg='honeydew4',
                                    command=self.quit)
        self.button_quit.grid(row=0, column=2, columnspan=2, sticky='NS')

        # Number buttons
        for i in range(self.h):
            for j in range(self.w):
                self.button_number[i][j] = tk.Button(master=self,
                                                    text='Row: {0}; Column: {1}'.format(i+1, j+1),
                                                    activebackground='gold',
                                                    bg='goldenrod',
                                                    command=None)
                self.button_number[i][j].grid(row=i+1, column=j, sticky='NSEW')

app = Application()
app.master.title('Task 1 application')
app.mainloop()


