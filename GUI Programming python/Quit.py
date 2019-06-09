#This program demostrate a QUIT BUTTON 

import tkinter
from tkinter import messagebox

class MyGUI:
        def __init(self):
            #create the main window widget
            self.main_window = tkinter.Tk()

            #Create a buttom widget 
            self.my_button = tkinter.Button(self.main_window, \ 
                                            text = 'Click Me!', \ 
                                            command = self.do_something)

            #create a quit button 
            self.quit_button = tkinter.Button (self.main_window,\
                                               text = 'Quit', \
                                               command = self.main_window.destroy)

            #pack the buttons
            self.my_button.pack()
            self.quit_button.pack()

            #Enter the tkinter main loop
            tkinter.mainloop()

#create do_something function 
        def do_something (self)
            tkinter.messagebox.showinfo('Response', \
                                        'Thanks for clicking the button')
#create and instance of class
my_gui = MYGUI()



