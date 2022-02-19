from tkinter import *
from fpdf import FPDF
import resources

# global variables
global WIDTH
global HEIGHT
global xAXIS
global yAXIS
global GEOMETRY

WIDTH = 1040 #set width of the app
HEIGHT = 585 #set the height of the app

class DearSanta:
    def __init__(self):
        self.splash = Tk()
        self.splash.overrideredirect(True)
        self.splash.resizable(0,0)
        xAXIS = int((self.splash.winfo_screenwidth()/2) -(WIDTH/2))
        yAXIS = int((self.splash.winfo_screenheight()/2) -(HEIGHT/2))
        GEOMETRY = f'{WIDTH}x{HEIGHT}+{xAXIS}+{yAXIS}'
        self.splash.geometry(GEOMETRY)
        
        bgImage = PhotoImage(file="resources/santa2.png")

        self.label = Label(self.splash, image=bgImage)
        self.label.place(relheight=1, relwidth=1)
        
        # set timer for splash screen to call the main function
        self.splash.after(7000, self.main)

        mainloop()

    def main(self):
        self.splash.destroy() # close the splash screen
        self.root = Tk() # instatiate the root window
        self.root.title('My Letter to Santa') # set window title
        # lauch window to the middle of the screen
        xAXIS = int((self.root.winfo_screenwidth()/2) -(WIDTH/2))
        yAXIS = int((self.root.winfo_screenheight()/2) -(HEIGHT/2))
        GEOMETRY = f'{WIDTH}x{HEIGHT}+{xAXIS}+{yAXIS}'
        self.root.geometry(GEOMETRY)
        self.root.resizable(0,0) # prevent window from being resized

        # define and set frames
        self.TopFrame = Frame(self.root)
        self.LeftFrame = LabelFrame(self.root, text='Questionaire', border=5)
        self.RightFrame = LabelFrame(self.root, text='The Letter', border=5)
        self.BottomFrame = Frame(self.root)

        self.lblTitle = Label(self.TopFrame, text='My Letter to Santa', font=('Roboto', 25, 'bold'))
        self.lblTitle.pack(padx=xAXIS/2, pady=15)

        self.lblSubTitle = Label(self.LeftFrame, text='Answer the following truthfully', font=('Roboto',14))
        self.lblSubTitle.pack(fill='x', padx=5, pady=(0,10))

        self.lblName = Label(self.LeftFrame, text='What is your name?', font=('Roboto',11))
        self.lblName.pack(fill='x', padx=5)
        self.entName = Entry(self.LeftFrame, width=20)
        self.entName.pack(fill='x', padx=5, pady=(0,10))
        self.lblAttitude = Label(self.LeftFrame, text='How was your attitude this year?', font=('Roboto',11))
        self.lblAttitude.pack(fill='x', padx=5)
        self.entAttitude = Entry(self.LeftFrame, width=20)
        self.entAttitude.pack(fill='x', padx=5, pady=(0,10))
        self.lblGift1 = Label(self.LeftFrame, text='Which gift is your first choice?', font=('Roboto',11))
        self.lblGift1.pack(fill='x', padx=5)
        self.entGift1 = Entry(self.LeftFrame, width=20)
        self.entGift1.pack(fill='x', padx=5, pady=(0,10))
        self.lblGift2 = Label(self.LeftFrame, text='Which gift is your second choice?', font=('Roboto',11))
        self.lblGift2.pack(fill='x', padx=5)
        self.entGift2 = Entry(self.LeftFrame, width=20)
        self.entGift2.pack(fill='x', padx=5, pady=(0,10))
        self.lblGift3 = Label(self.LeftFrame, text='Which gift is your third choice?', font=('Roboto',11))
        self.lblGift3.pack(fill='x', padx=5)
        self.entGift3 = Entry(self.LeftFrame, width=20)
        self.entGift3.pack(fill='x', padx=5, pady=(0,10))
        self.lblDrink = Label(self.LeftFrame, text='What drink will you prepare for Santa?', font=('Roboto',11))
        self.lblDrink.pack(fill='x', padx=5)
        self.entDrink = Entry(self.LeftFrame, width=20)
        self.entDrink.pack(fill='x', padx=5, pady=(0,10))
        self.lblSnack = Label(self.LeftFrame, text='What snacks will you prepare for Santa?', font=('Roboto',11))
        self.lblSnack.pack(fill='x', padx=5)
        self.entSnack = Entry(self.LeftFrame, width=20)
        self.entSnack.pack(fill='x', padx=5, pady=(0,10))
        
        self.txtEditor = Text(self.RightFrame, width=50, height=16, wrap = 'word', font=('Courier', 18))
        self.txtEditor.pack(fill='both', expand='yes', side='left', padx=5, pady=5)

        #Pack the Frames
        self.TopFrame.pack(fill='both', padx=5)
        self.LeftFrame.pack(fill='both', expand=1, side='left', padx=5)
        self.RightFrame.pack(fill='both', expand=1, side='left', padx=5)
        self.BottomFrame.pack(fill='both', expand=1, padx=5, pady=5)

        #Buttons
        self.btnSubmit = Button(self.LeftFrame, text='SUBMIT', command=self.submit)
        self.btnPopulate = Button(self.LeftFrame, text='POPULATE', command=self.populate)
        self.btnClear = Button(self.LeftFrame, text='CLEAR', command=self.clear)
        self.btnExit = Button(self.LeftFrame, text='EXIT', command=self.root.destroy)

        #Pack the buttons
        self.btnSubmit.pack(side='left', padx=(5,0), pady=(0,5))
        self.btnPopulate.pack(side='left', padx=(5,0), pady=(0,5))
        self.btnClear.pack(side='left', padx=(5,0), pady=(0,5))
        self.btnExit.pack(side='left', padx=(5,5), pady=(0,5))

         # Create and pack widgets for frmCopyright frame.
        self.lblCopyright = Label(self.BottomFrame, background="lightgreen", text="\N{COPYRIGHT SIGN} 2021 | shkungulio | All rights reserved")
        self.lblCopyright.pack()

        # initialize the form's default state
        self.defaults()

    def submit(self):
        
        name = self.entName.get().title()
        attitude = self.entAttitude.get().lower()
        gift1 = self.entGift1.get().upper()
        gift2 = self.entGift2.get().lower()
        gift3 = self.entGift3.get().lower()
        drink = self.entDrink.get().lower()
        snack = self.entSnack.get().lower()

        msg = resources.Message(attitude, gift2, gift3, gift1, drink, snack, name)

        self.txtEditor.config(state='normal')
        self.txtEditor.delete(1.0, 'end')
        self.txtEditor.insert(1.0, msg)
        self.entName.config(state='disabled')
        self.entAttitude.config(state='disabled')
        self.entGift1.config(state='disabled')
        self.entGift2.config(state='disabled')
        self.entGift3.config(state='disabled')
        self.entDrink.config(state='disabled')
        self.entSnack.config(state='disabled')
        self.txtEditor.config(state='disabled')

        myLetter = open('myLetter.txt', 'w')
        myLetter.write(self.txtEditor.get(3.0, END))


    def populate(self):
        
        pdf = resources.PDF('P', 'mm', 'Letter')
        pdf.set_auto_page_break(auto=True, margin=35)
        pdf.add_page()
        pdf.set_font('Courier', 'B', 25)

        myLetter = open('myLetter.txt', 'r')

        for line in myLetter:
            pdf.multi_cell(200, 10, txt=line, align='L')
           
        pdf.output('myLetter.pdf', 'F')
        

    def clear(self):
        #unlock the form so that contents can be deleted
        self.txtEditor.config(state='normal')
        self.entName.config(state='normal')
        self.entAttitude.config(state='normal')
        self.entGift1.config(state='normal')
        self.entGift2.config(state='normal')
        self.entGift3.config(state='normal')
        self.entDrink.config(state='normal')
        self.entSnack.config(state='normal')
        self.txtEditor.config(state='normal')

        # delete everything from the form
        self.entName.delete(0,'end')
        self.entAttitude.delete(0,'end')
        self.entGift1.delete(0,'end')
        self.entGift2.delete(0,'end')
        self.entGift3.delete(0,'end')
        self.entDrink.delete(0,'end')
        self.entSnack.delete(0,'end')
        self.txtEditor.delete(1.0,'end')

        # call the default state of the form
        self.defaults()

    def defaults(self): # once called this will set as default state for the form
        self.entName.focus()
        self.txtEditor.config(state='disabled')


if __name__ == '__main__':
    
    main = DearSanta()