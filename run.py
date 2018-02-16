#!/usr/bin/env python3
'''
Random number generator application
'''

import random
import tkinter

# Range of random integers
min_randint = 1
max_randint = 20

# Generate a random integer
randint_as_int = random.randint(min_randint, max_randint)
randint_as_str = str(randint_as_int)

# Create a new graphical user interface (GUI) using tkinter
gui = tkinter.Tk()

# Place the random integer as text inside the GUI window
window = tkinter.Label(gui, text=randint_as_str)
window.pack()

# Show the GUI to the user. Start the GUI function 'mainloop()'.
print(" - NOTE: The GUI window is very small. Check the top left of the screen.")
gui.mainloop()