#This program displays a label with text.

import tkinter

class MyGUI:
    def __init__(self):
        #Create a window widget 
        self.main_window = tkinter.Tk()

        #Create a Label widget containing the text 'Helloworld'
        self.label1= tkinter.Label (self.main_window, \
                                    text = 'Hello World!')
        self.label2= tkinter.Label (self.main_window, \
                                     text = 'This is a GUI program')

        #Call the labels widget's pack method (COMPACTS ALL IN A WINDOW)
        self.label1.pack()
        self.label2.pack()

        #Enter the tkinter main loop
        tkinter.mainloop()

#create an intance of the MYGUI class.
my_gui = MyGUI()
