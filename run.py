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
    roll_counter = 0
    min_rand = 1
    max_rand = 20
    gui_width = 24
    gui_height = 3
    label = None
    font = ("Helvetica", 24)

    def __init__(self, parent=None):
        w = self.gui_width
        h = self.gui_height
        f = self.font

        tk.Frame.__init__(self, parent)
        tk.Frame.pack(self)
        self.label = tk.Label(self, text='--- ---', font=f, width=w, height=h)
        self.label.pack()
        self.winfo_toplevel().title('TK-Talus')
        tk.Button(self, text='Roll', font=f, width=w, command= lambda: self.generate_randint()).pack()

    def generate_randint(self):
        '''
        Generate a random integer within the desired range
        '''
        random_integer = random.randint(self.min_rand, self.max_rand)
        self.roll_counter = self.roll_counter + 1
        self.update_label(random_integer)
        self.update_title()

    def update_label(self, random_integer):
        '''
        Update the GUI to display the updated random integer
        '''
        self.label.config(text=str(random_integer))

    def update_title(self):
        '''
        Update the GUI to title bar to display the updated counter
        '''
        dice_num = self.max_rand
        roll_num = self.roll_counter
        title_string = 'TK-Talus      |      d%d, roll %d' % (dice_num, roll_num)
        self.winfo_toplevel().title(title_string)

if __name__ == '__main__':
    main()
