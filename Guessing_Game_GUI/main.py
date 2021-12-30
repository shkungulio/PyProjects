#!/bin/env python3

import random
from tkinter import *
from tkinter.font import BOLD


class GuessGame:
    def __init__(self):
        self.root = Tk()
        self.root.title('Guessing Game')
        self.root.geometry('620x465')
        self.root.resizable(FALSE, FALSE)
        self.root.iconbitmap('mark.ico')

        self.frmMain = LabelFrame(self.root, border=5)
        self.frmMain.place(relheight=0.9, relwidth=0.9, relx=0.05, rely=0.05)

        self.frmLeft = LabelFrame(self.frmMain, text='Set Boundaries: Enter Min & Max Values')
        self.frmLeft.grid(row=0, column=0, columnspan=3, padx=5, pady=5, sticky=W)
        self.frmRight = LabelFrame(self.frmMain, text='Guess the number')
        self.frmRight.grid(row=0, column=3, columnspan=2, padx=5, pady=5, sticky=W)
        self.frmBottom = LabelFrame(self.frmMain, text='Display information')
        self.frmBottom.grid(row=5, column=0, columnspan=5, padx=5, sticky=W)
        self.frmButtons = LabelFrame(self.frmMain, text='')
        self.frmButtons.grid(row=9, column=0, columnspan=5, padx=5, sticky=W)
        

        self.lblMinBoundary = Label(self.frmLeft, text='Minimum:')
        self.lblMinBoundary.grid(row=1, column=0, padx=5, pady=5)
        self.entMinBoundary = Entry(self.frmLeft)
        self.entMinBoundary.grid(row=1, column=1)
        self.lblMaxBoundary = Label(self.frmLeft, text='Maximum:')
        self.lblMaxBoundary.grid(row=2, column=0, padx=5, pady=5)
        self.entMaxBoundary = Entry(self.frmLeft)
        self.entMaxBoundary.grid(row=2, column=1)
        self.btnSet = Button(self.frmLeft, text='SET', width=10, command=self.set_bounds)
        self.btnSet.grid(row=2, column=2, padx=5, pady=5)

        self.lblEmpty = Label(self.frmRight)
        self.lblEmpty.grid(row=1, padx=5, pady=5, sticky=W)
        self.entGuess = Entry(self.frmRight)
        self.entGuess.grid(row=2, column=1)
        self.btnGuess = Button(self.frmRight, text='GUESS', width=10, command=self.guess)
        self.btnGuess.grid(row=2, column=4, padx=5, pady=5, sticky=W)

        self.txtInfo = Text(self.frmBottom, font=('Courier', 15), width=43, height=2)
        self.txtInfo.grid(row=6, column=0, padx=5, pady=(5,0))
        self.txtDisplay = Text(self.frmBottom, font=('Courier', 15), width=43, height=8)
        self.txtDisplay.grid(row=7, column=0, padx=5, pady=(0,5))

        self.btnClear = Button(self.frmButtons, text='CLEAR', width=10, command=self.clear)
        self.btnClear.grid(row=9, column=0, padx=5, pady=5, sticky=W)
        self.lblEmpty2 = Label(self.frmButtons, width=50)
        self.lblEmpty2.grid(row=9, column=1, columnspan=3)
        self.btnExit = Button(self.frmButtons, text='EXIT', width=10, command=self.root.destroy)
        self.btnExit.grid(row=9, column=4, padx=5, pady=5, sticky=E)

        
        self.defaults()
        
        mainloop()
        
    def set_bounds(self):
        global minimum
        global maximum
        global random_number
        
        try:
            minimum = int(self.entMinBoundary.get())
            maximum = int(self.entMaxBoundary.get())
            if minimum < maximum:
                self.entMinBoundary.config(state='disabled')
                self.entMaxBoundary.config(state='disabled')
                self.btnSet.config(state='disabled')
                self.entGuess.config(state='normal')
                self.entGuess.focus()
                self.txtInfo.config(state='normal', bg='#84BF04', fg='#FFFFFF')
                
                self.txtInfo.delete(1.0,'end')
                self.txtDisplay.delete(1.0,'end')
                msg = f'I am thinking of a number between {minimum} and \n{maximum}, can you guess it?: \n'
                self.txtInfo.insert(END, msg)

                self.btnGuess.config(state='normal')
                random_number = random.randint(minimum, maximum) # Generate a random number to be guessed
            else:
                self.txtDisplay.config(state='normal', bg='#990000', fg='#FFFFFF')
                msg = f'You have set minimum value larger than \nmaximum value! Try Again!\n'
                self.txtDisplay.insert(END, msg)
                self.entMinBoundary.delete(0,'end')
                self.entMaxBoundary.delete(0,'end')
                self.entMinBoundary.focus()
        except Exception:
            self.txtInfo.config(state='normal', bg='#990000', fg='#FFFFFF')
            self.txtInfo.delete(1.0,'end')
            msg = f'There was problem retrieving that value! \nTry Again!\n'
            self.txtInfo.insert(END, msg)
            self.entMinBoundary.delete(0,'end')
            self.entMaxBoundary.delete(0,'end')
            self.entMinBoundary.focus()

    def guess(self):
        self.entMinBoundary.config(state='normal')
        self.entMaxBoundary.config(state='normal')
        
        try:
            guess = int(self.entGuess.get())
            self.entMinBoundary.config(state='disabled')
            self.entMaxBoundary.config(state='disabled')
            self.txtDisplay.config(state='normal', bg='#84BF04', fg='#FFFFFF')
            if guess < minimum or guess > maximum:
                msgOut = f'{guess} is out of boundary, Try Again\n'
                self.txtDisplay.insert('end', msgOut)
                self.txtDisplay.config(state='disabled', bg='#990000')
                self.entGuess.delete(0,'end')
                self.entGuess.focus()
            elif guess < random_number: # Check if the guessed number is lower than the generated guess
                msgL = f'Sorry {guess} is low, Guess Again!\n'
                self.txtDisplay.insert(END, msgL)
                self.txtDisplay.config(bg='#E6E600')
                self.entGuess.delete(0,'end')
            elif guess > random_number: # Check if the guessed number is higher than the generated guess
                msgH = f'Sorry {guess} is high, Guess Again!\n'
                self.txtDisplay.insert(END, msgH)
                self.txtDisplay.config(bg='#E6E600')
                self.entGuess.delete(0,'end')
            else:
                msg = f'\nCONGRATULATIONS!!! the guess is {guess}\n'
                self.txtDisplay.delete(1.0,'end')
                self.txtDisplay['font'] = ('Roboto', 16, BOLD)
                self.txtDisplay.insert(END, msg)
                
        except Exception:
            self.txtDisplay.config(state='normal', bg='#990000', fg='#FFFFFF')
            msg = f'There was problem retrieving that value! \nGuess Again!\n'
            self.txtDisplay.insert(END, msg)
            self.entGuess.delete(0,'end')
            self.entGuess.focus()

    def clear(self):
        
        self.entMinBoundary.config(state='normal')
        self.entMaxBoundary.config(state='normal')
        self.btnSet.config(state='normal')
        self.entMinBoundary.delete(0,'end')
        self.entMaxBoundary.delete(0,'end')
        self.entGuess.delete(0,'end')
        self.txtInfo.delete(1.0,'end')
        self.txtDisplay.delete(1.0,'end')
        
        self.defaults()

    def defaults(self):
        '''
        This function will be called when the app loads
        '''
        self.entMinBoundary.focus()
        self.entGuess.config(state='disabled')
        self.txtInfo.config(state='disabled', bg="#001A33")
        self.txtDisplay.config(state='disabled', bg="#001A33")
        self.btnGuess.config(state='disabled')


if __name__ == '__main__':
    GuessGame()