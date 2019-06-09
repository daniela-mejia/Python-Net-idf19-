#This program uses the side='left' argument with  the pack methid change the layout of the widgets

import tkinter

class MyGUI:

    def __init__(self):
        #Create the  main window widget

        self.main_window = tkinter. Tk()

        #create a two label widgets
        self.label1 = tkinter.label (self.main_window, \
                                     text = 'Hello World!')
        self.label2 = tkinter.label (self.main_window, \
                                     text = 'This is my GUI program')

        #Call both label widgets pack method

        self.label1.pack(side='left')
        self.label2.pack(side='left')

        #Enter the tkinter main loop
        tkinter.mainloop()

#create an instance of the MyGUI class
        my_gui = MyGUI()
