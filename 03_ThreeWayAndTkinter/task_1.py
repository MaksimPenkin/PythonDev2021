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
        for i in range(self.h):
            self.rowconfigure(i, weight=1)
        for j in range(self.w):
            self.columnconfigure(j, weight=1)
        
        for i in range(self.h):
            for j in range(self.w):
                self.button_number[i][j] = tk.Button(master=self, text='Row: {0}; Column: {1}'.format(i+1, j+1), command=None)
                self.button_number[i][j].grid(row=i, column=j, sticky='NSEW')

app = Application()
app.master.title('Task 1 application')
app.mainloop()


