#!/usr/bin/env python3
'''
Random number generator application
'''

import random
import tkinter

def main():
    '''
    This is the main function that calls all the other functions in the script
    '''
    display_gui()

def generate_randint(label):
    '''
    Generate a random integer within the desired range
    '''
    minimum = 1
    maximum = 20

    random_integer = random.randint(minimum, maximum)
    label.config(text=str(random_integer))

def display_gui():
    '''
    Configure and display a GUI window to show a random integer
    '''
    width = 40
    height = 3

    gui = tkinter.Tk()
    label = tkinter.Label(gui, text='-- --', width=width, height=height)
    label.pack()
    button = tkinter.Button(gui, text='ROLL', width=width, command= lambda: generate_randint(label))
    button.pack()

    gui.mainloop()

if __name__ == '__main__':
    main()
