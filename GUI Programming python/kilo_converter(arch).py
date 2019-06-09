#this program converts distances in km to miles.
#The result is displayed in an info dialog box

import tkinter
from tkinter import messagebox

class kiloConverterGUI:
    def __init__(self):

        #create the main window
        self.main_window = tkinter.Tk()

        #create two frames to group widgets
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        #create the widgets for the top frame 
        self.prompt_label = tkinter.Label(self.top_frame, \
                                          text = 'Enter a distance in km: ')
        self.kilo_entry = tkinter.Entry(self.top_frame, \ 
                                        width=10)
        #Pack the top frame's widgets
        self.prompt_label.pack(side='left')
        self.kilo_entry.pack(side='left')

        #create the button widgets for the bottom frame
        self.calc_button = tkinter.Button(self.bottom_frame, \
                                           text = 'covert', \
                                           command = self.convert)
        self.quit_button = tkinter.Button(self.bottom_frame, \ 
                                          text='Quit', \
                                          command = self.main_window.destroy)
        