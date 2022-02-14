# import modules
from textwrap import fill
from tkinter import *
import resources

# set global variables
global WIDTH
global HEIGHT
global xAXIS
global yAXIS
global GEOMETRY

# set the width and height of the app
WIDTH = 1040
HEIGHT = 585

class Weather:
    def __init__(self):
        self.splash = Tk()
        self.splash.overrideredirect(True)
        self.splash.resizable(0,0)
        xAXIS = int((self.splash.winfo_screenwidth()/2) -(WIDTH/2))
        yAXIS = int((self.splash.winfo_screenheight()/2) -(HEIGHT/2))
        GEOMETRY = f'{WIDTH}x{HEIGHT}+{xAXIS}+{yAXIS}'
        self.splash.geometry(GEOMETRY)

        #create canvas to hold all main label that will hold background image
        self.canvas = Canvas(self.splash)
        self.canvas.place(relheight=1, relwidth=1)
        
        bgImage = PhotoImage(file="resources/climate.png")

        self.lblMain = Label(self.canvas, image=bgImage)
        self.lblMain.place(relheight=1, relwidth=1)

        self.lblTitle = Label(self.lblMain, text='Weather App', font=('Roboto', 40, 'bold'), bg='#010020', fg='red')
        self.lblTitle.pack(fill='both', pady=(425, 100), padx=300)
        
        # set timer for splash screen to call the main function
        self.splash.after(10000, self.main)

        mainloop()

    def main(self):
        self.splash.destroy() # close the splash screen
        self.root = Tk()
        self.root.title('Weather Application')
        
        xAXIS = int((self.root.winfo_screenwidth()/2) -(WIDTH/2))
        yAXIS = int((self.root.winfo_screenheight()/2) -(HEIGHT/2))
        GEOMETRY = f'{WIDTH}x{HEIGHT}+{xAXIS}+{yAXIS}'
        self.root.geometry(GEOMETRY)
        self.root.resizable(0,0)
                
        #create canvas to hold all main label that will hold background image
        self.canvas = Canvas(self.root)
        self.canvas.place(relheight=1, relwidth=1)
        
        self.bgImage = PhotoImage(file="resources/lightning.png")

        self.lblMain = Label(self.canvas, image=self.bgImage)
        self.lblMain.place(relheight=1, relwidth=1)

        #Create frames to hold widgets
        self.frmTop = LabelFrame(self.lblMain, width=40, background='lightgreen') #top frame for search input
        self.frmTop.pack(pady=(100,50))
        self.frmBottom = LabelFrame(self.lblMain, width=40, background='#7F9200') #bottom frame to display weather information
        self.frmBottom.pack()
        self.frmCopyright = Label(self.lblMain, background='lightgreen') #copyright label to show copyright information
        self.frmCopyright.pack(fill='both', pady=(75,0))

        #Create widgets
        self.entCity = Entry(self.frmTop, width=32, font=('Roboto', 20))
        self.entCity.pack(padx=5, pady=5, fill='both', side='left')
        self.btnSearch = Button(self.frmTop, text='Search', font=('Roboto', 20), command=lambda: self.search())
        self.btnSearch.pack(padx=5, pady=5, fill='both', side='left')
        self.txtInfo = Text(self.frmBottom, width=40, height=8, wrap='word', font=('Roboto', 20))
        self.txtInfo.pack(padx=5, pady=5, fill='both', side='left')

        self.lblCopyright = Label(self.frmCopyright, bg="lightgreen", 
                                    text="\N{COPYRIGHT SIGN} 2022 | shkungulio | All rights reserved") #copyright information
        self.lblCopyright.pack()

        self.defaults() #call default state of the app
        

    def search(self):
        self.txtInfo.config(state='normal')
        self.city = self.entCity.get()
                
        # display the weather informations
        self.txtInfo.delete(1.0, END) # clear the text box
        self.txtInfo.insert(END, resources.searchWeather(self.city)) # enter information to display
        self.defaults() #call default fuction to disable text box.

    def defaults(self):
        self.entCity.delete(0, END)
        self.entCity.insert(0, 'Enter City')
        self.entCity.focus()
        self.txtInfo.config(state='disabled')


if __name__ == '__main__':
    # create Weather class object
    Weather()