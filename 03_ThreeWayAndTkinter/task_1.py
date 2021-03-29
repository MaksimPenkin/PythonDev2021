""" 
 @author   Maksim Penkin
"""

import tkinter as tk


class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid(sticky='NEWS')
        self.h = 4
        self.w = 4
        self.button_number = [[None]*self.w]*self.h
        for i in range(self.h):
            for j in range(self.w):
                self.button_number[i][j] = tk.Button(master=self, text='Row: {0}; Column: {1}'.format(i+1, j+1), command=None)
                self.button_number[i][j].grid(row=i, column=j, sticky='NEWS')

app = Application()
app.master.title('Task 1 application')
app.mainloop()


