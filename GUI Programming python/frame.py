#This program creates labels ini two different frames

import tkinter

class MyGUI:
    def __init__(self):
        #creates the main window widget
        self.main_window = tkinter.Tk()

        #create two frames, one for the top of the window, and one for the bottom.
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        #pack the labels in top frame
        
        #create three Label widgets for the top frame
        self.Label1 = tkinter.Label (self.top_frame, \
                                     text = 'Winken')
        self.Label2 = tkinter.Label (self.top_frame, \
                                     text = 'Blinken')
        self.Label3 = tkinter.Label (self.top_frame, \
                                     text = 'Nod')

        #pack the labels in top frame
        self.label1.pack(side='Top')
        self.label2.pack(side='Top')
        self.label3.pack(side='Top')

        #create three label widgets for bottom frame
        self.Label4 = tkinter.Label (self.top_frame, \
                                     text = 'Winken')
        self.Label5 = tkinter.Label (self.top_frame, \
                                     text = 'Blinken')
        self.Label6 = tkinter.Label (self.top_frame, \
                                     text = 'Nod')

               
        #pack method

        self.label4.pack(side='left')
        self.label5.pack(side='left')
        self.label6.pack(side='left')

        #Yes, we have to pack the frames too!
        self.top_frame.pack()
        self.bottom_frame.pack()
        
        #enter the tkinter main loop
        tkinter.mainloop()

#create an instance of the MyGUI class
my_gui = MyGUI()
        
