#!/bin/eny python3

import sys
import time
from tkinter import *
class DigitalClock:
    def __init__(self):
        self.root = Tk()
        self.root.title('Digital Clock')
        self.root.geometry('600x400')
        self.root.resizable(False, False)
        self.root.config(bg='lightgreen')

        self.frmMain = LabelFrame(self.root, text='')
        self.frmMain.place(relwidth=0.9, relheight=0.9, rely=0.05, relx=0.05)

        self.lblClock = Label(self.frmMain, font=('Roboto', 60, "bold"), relief='sunken', border=50, fg='red')
        self.lblClock.pack(fill=BOTH, expand=1)
        self.digital_clock()

        mainloop()

    def digital_clock(self):
        current_time = time.strftime('%H:%M:%S')
        self.lblClock.config(text=current_time)
        self.lblClock.after(200, self.digital_clock)


if __name__ == '__main__':
    DigitalClock()