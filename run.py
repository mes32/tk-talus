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
    random_integer = generate_randint()
    display_gui(random_integer)

def generate_randint():
    '''
    Generate a random integer within the desired range
    '''
    minimum = 1
    maximum = 20

    return random.randint(minimum, maximum)

def display_gui(random_integer):
    '''
    Configure and display a GUI window to show a random integer
    '''
    width_padding = 10
    height_lines = 5

    gui = tkinter.Tk()
    window = tkinter.Label(gui, text=str(random_integer), width=width_padding, height=height_lines)
    window.pack()
    gui.mainloop()

if __name__ == '__main__':
    main()
