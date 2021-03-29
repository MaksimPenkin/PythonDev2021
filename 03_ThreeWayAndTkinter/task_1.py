""" 
 @author   Maksim Penkin
"""

import tkinter as tk
import random


class Application(tk.Frame):
    def configure_grid(self):
        self.grid(sticky='NEWS')
        self.play_Buttons_position = list(range(self.N*self.N))
        self.play_Buttons = [None]*(self.N*self.N - 1)
        # https://stackoverflow.com/questions/7591294/how-to-create-a-self-resizing-grid-of-buttons-in-tkinter/38809894
        root = self.winfo_toplevel()
        root.rowconfigure(0, weight=1)
        root.columnconfigure(0, weight=1)
        for i in range(self.N+1):
            self.rowconfigure(i, weight=1)
        for j in range(self.N):
            self.columnconfigure(j, weight=1)

    def create_new_Button(self):
        self.new_Button = tk.Button(master=self,
                                    text='New',
                                    activebackground='green yellow',
                                    bg='lime green',
                                    command=self.new_Button_handler)
        self.new_Button.grid(row=0, column=0, sticky='NEWS')
    
    def create_quit_Button(self):
        self.quit_Button = tk.Button(master=self,
                                    text='Quit',
                                    activebackground='honeydew3',
                                    bg='honeydew4',
                                    command=self.quit)
        self.quit_Button.grid(row=0, column=3, sticky='NEWS')

    def create_play_Buttons(self):
        # foreach play button
        for idx in range(self.N*self.N - 1):
            loc = self.play_Buttons_position[idx] # take play button position on the grid
            i, j = loc // self.N, loc % self.N
            self.play_Buttons[idx] = tk.Button(master=self,
                                                text='{}'.format(idx+1),
                                                activebackground='gold',
                                                bg='goldenrod',
                                                command=None)
            # set play button position on the grid
            self.play_Buttons[idx].grid(row=i+1, column=j, sticky='NEWS')

    def new_Button_handler(self):
        self.play_Buttons_position = random.sample(self.play_Buttons_position, self.N*self.N) # shuffle play buttons positions
        # foreach play button
        for idx in range(self.N*self.N - 1):
            loc = self.play_Buttons_position[idx] # take play button position on the grid
            i, j = loc // self.N, loc % self.N
            # set play button position on the grid
            self.play_Buttons[idx].grid(row=i+1, column=j, sticky='NEWS')

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.victory = False
        self.N = 4
        # Grid configuration
        self.configure_grid()
        # New button
        self.create_new_Button()
        # Quit button
        self.create_quit_Button()
        # Number buttons
        self.create_play_Buttons()

if __name__ == "__main__":
    app = Application()
    app.master.title('Task 1 application')
    app.mainloop()


