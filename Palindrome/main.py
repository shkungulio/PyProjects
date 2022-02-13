#!/bin/env python3

"""
A palindrome is a word, number, phrase, or other sequence of characters 
which reads the same backward as forward, such as madam or racecar.
"""
from tkinter import *

# Create a palindrome class
class Palindrome:
    def __init__(self):
        self.root = Tk()
        self.root.title('Palindrome App') # set title of the app
        self.root.geometry("350x300") # set the dimensions of the app
        self.root.resizable(FALSE, FALSE) # prevent the app from being resized
        self.root.protocol("WM_DELETE_WINDOW", self.disable_event)

        # Create and pack to hold Canvas to hold all frames of the App.
        self.canvas = Canvas(self.root)
        self.canvas.pack()

        # Create frames to hold widgets.
        self.frmMain = LabelFrame(self.canvas, text="Is it Palindrome?", border=5)
        self.frmTop = LabelFrame(self.frmMain, text="Enter an Input")
        self.frmMiddle = LabelFrame(self.frmMain, text="Display Response")
        self.frmBottom = LabelFrame(self.frmMain)
        self.frmCopyright = Frame(self.root, bg="lightgreen")
        
        # Create and pack widgets for frmTop frame.
        self.entText = Entry(self.frmTop, width=100)
        self.entText.focus()
        self.entText.pack(side=LEFT, pady=5, padx=5)
        
        # Create and pack widgets for frmMiddle frame.
        self.response = StringVar()
        self.response.set('')
        self.lblResponse = Label(self.frmMiddle, font=('Roboto, 13'), borderwidth=8, 
                                    relief= RIDGE, textvariable=self.response)
        self.lblResponse.pack(fill=BOTH, expand=YES, padx=5, pady=5)

        # Create and pack widgets for frmBottom frame.
        self.btnClear = Button(self.frmBottom, text="CLEAR", width=8, command=self.clear)
        self.btnCheck = Button(self.frmBottom, text="CHECK", width=8, command=self.isPalindrome)
        self.btnExit = Button(self.frmBottom, text="EXIT", width=10, command=self.root.destroy)
        self.btnClear.pack(side=LEFT, padx=(0,5))
        self.btnCheck.pack(side=LEFT, padx=5)
        self.btnExit.pack(side=LEFT, padx=(5,0))

        # Create and pack widgets for frmCopyright frame.
        self.lblCopyright = Label(self.frmCopyright, bg="lightgreen", 
                                    text="\N{COPYRIGHT SIGN} 2021 | shkungulio | All rights reserved")
        self.lblCopyright.pack()

        # Pack all the frames
        self.frmMain.place(relheight=0.9, relwidth=0.9, relx=0.05, rely=0.05)
        self.frmTop.pack(fill=BOTH, expand=NO)
        self.frmMiddle.pack(fill=BOTH, expand=YES)
        self.frmBottom.pack(fill=BOTH)
        self.frmCopyright.pack(fill=BOTH, side='bottom')

        # Run the App.
        mainloop()
        
    def isPalindrome(self):
        
        try:
            # Create messages to be displayed depending to 
            # input whether is palindrome or not palindrome
            yesMessage = 'YES! \n\"' + self.entText.get() + '\"\n does have \nPalindrome pattern'
            noMessage = 'NO! \n\"'  + self.entText.get() + '\"\n does not have \nPalindrome pattern'
            # Get the input from input field, convert it to lower case string, 
            # and assign it to variable ans
            ans = str(self.entText.get().lower())

            if ans == ans[::-1]: # chechk whether the string can be read backward as forward
                self.response.set(yesMessage) # display the message if it is palindrome
            else:
                self.response.set(noMessage) # display the message if it not palindrome
        except Exception:
            warning = "There was problem retrieving that value! \n Try Again!"
            self.response.set(warning)

    def clear(self):
        # The function to clear the entry input and response display
        self.entText.delete(0, END)
        self.response.set(" ")
        self.entText.focus()

    def disable_event(self):
        pass

if __name__ == "__main__":
    Palindrome()