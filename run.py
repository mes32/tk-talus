#!/usr/bin/env python3
'''
Random number generator application
'''

import random
import tkinter as tk

def main():
    gui = TalusFrame()
    gui.mainloop()

class TalusFrame(tk.Frame):
    '''
    Extend tkinter Frame class to display a random number generator
    '''

    def __init__(self, parent=None):
        width = 40
        height = 3

        tk.Frame.__init__(self, parent)
        tk.Frame.pack(self)
        label = tk.Label(self, text='-- --', width=width, height=height)
        label.pack()
        tk.Button(self, text='ROLL', width=width, command= lambda: generate_randint(label)).pack()

def generate_randint(label):
    '''
    Generate a random integer within the desired range
    '''
    minimum = 1
    maximum = 20

    random_integer = random.randint(minimum, maximum)
    label.config(text=str(random_integer))

if __name__ == '__main__':
    main()
