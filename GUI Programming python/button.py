import tkinter
from tkinter import messagebox

class MyGUI:
    def __init__(self):
        #create the main window widget
        
        self.main_window = tkinter.Tk()

        #create a Button widget. The text 'Click Me! do something when button clicked
        self.my_button = tkinter.Button(self.main_window, \
                                        text = 'click Me!', \
                                        command = self.do_something) #call function do_something

        #pack the button
        self.my_button.pack()

        #enter tkinter main loop

        tkinter.mainloop()

        #do_something func

    def do_something(self):
            #Display an info dialog box
        tkinter.messagebox.showinfo('Response', \
                                    'Thanks for clicking')
#Create an instance of MyGUI
my_gui = MyGUI()
