from tkinter import *
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
        self.root = Tk()
        self.root.title('My Letter to Santa')
        #self.root.overrideredirect(True)
        xAXIS = int((self.root.winfo_screenwidth()/2) -(WIDTH/2))
        yAXIS = int((self.root.winfo_screenheight()/2) -(HEIGHT/2))
        GEOMETRY = f'{WIDTH}x{HEIGHT + 10}+{xAXIS}+{yAXIS}'
        self.root.geometry(GEOMETRY)
        self.root.resizable(0,0)

if __name__ == '__main__':
    
    main = DearSanta()