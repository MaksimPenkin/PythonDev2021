""" 
 @author   Maksim Penkin
"""

import tkinter as tk


class Application(tk.Frame):
    def create_new_Button(self):
        self.new_Button = tk.Button(master=self,
                                    text='New',
                                    activebackground='green yellow',
                                    bg='lime green',
                                    command=None)
        self.new_Button.grid(row=0, column=0, columnspan=2, sticky='NS')
    
    def create_quit_Button(self):
        self.quit_Button = tk.Button(master=self,
                                    text='Quit',
                                    activebackground='honeydew3',
                                    bg='honeydew4',
                                    command=self.quit)
        self.quit_Button.grid(row=0, column=2, columnspan=2, sticky='NS')

    def create_number_Buttons(self):
        for i in range(self.N):
            for j in range(self.N):
                if not ((i == (self.N - 1)) and (j == (self.N - 1))):
                    self.number_Buttons[i][j] = tk.Button(master=self,
                                                        text='{}'.format(i*self.N + j + 1),
                                                        activebackground='gold',
                                                        bg='goldenrod',
                                                        command=None)
                    self.number_Buttons[i][j].grid(row=i+1, column=j, sticky='NEWS')

    def configure_grid(self):
        self.grid(sticky='NEWS')
        self.number_Buttons = [[None]*self.N]*self.N
        
        # https://stackoverflow.com/questions/7591294/how-to-create-a-self-resizing-grid-of-buttons-in-tkinter/38809894
        root = self.winfo_toplevel()
        root.rowconfigure(0, weight=1)
        root.columnconfigure(0, weight=1)
        for i in range(self.N+1):
            self.rowconfigure(i, weight=1)
        for j in range(self.N):
            self.columnconfigure(j, weight=1)
    
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.victory = False
        self.N = 4
        # Grid cinfiguration
        self.configure_grid()
        # New button
        self.create_new_Button()
        # Quit button
        self.create_quit_Button()
        # Number buttons
        self.create_number_Buttons()

app = Application()
app.master.title('Task 1 application')
app.mainloop()


