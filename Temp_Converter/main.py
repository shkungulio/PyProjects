#!/bin/env python3
###########
# imports #
###########

from tkinter import *

class TempConverter:
    def __init__(self):
        self.root = Tk()
        self.root.title("Temperature Converter")
        self.root.resizable(FALSE, FALSE)

        self.canvas = Canvas(self.root, width=300, height=360)
        self.canvas.pack()
        self.frmMain = LabelFrame(self.canvas, text='Temperature Convertion', padx=5, pady=5, border=5)
        self.frmMain.place(relwidth=0.9, relheight=0.9, relx=0.05, rely=0.05)

        """Create LabelFrames to hold associated widgets"""
        self.frmDataEntry = Frame(self.frmMain, pady=5, padx=5)
        self.frmFahrenheit = LabelFrame(self.frmMain, text='To \N{DEGREE SIGN}Fahrenheit', pady=5, padx=5)
        self.frmCelsius = LabelFrame(self.frmMain, text='To \N{DEGREE SIGN}Celsius', pady=5, padx=5)
        self.frmKelvin = LabelFrame(self.frmMain, text='To \N{DEGREE SIGN}Kelvin', pady=5, padx=5)
        self.frmMessage = LabelFrame(self.frmMain, text='Message', pady=5, padx=5)

        """Create widgets for the frmDataEntry frame"""
        self.entInput = Entry(self.frmDataEntry)
        self.option = ["\N{DEGREE SIGN}C", "\N{DEGREE SIGN}F", "\N{DEGREE SIGN}K"]
        self.value = StringVar()
        self.value.set("\N{DOWNWARDS BLACK ARROW}")
        self.tempSign = OptionMenu(self.frmDataEntry, self.value, *self.option)
        self.btnConvert = Button(self.frmDataEntry, width=15, text='Convert', command=self.convert)

        """Pack the widgets for the frmDataEntry frame."""
        self.entInput.pack(side=LEFT)
        self.tempSign.pack(side=LEFT)
        self.btnConvert.pack(side=LEFT)

        """Create the widgets for the frmCelsius frame"""
        self.tempCelsius = StringVar()
        self.lblCelsius = Label(self.frmCelsius, font=('Roboto', 16), textvariable=self.tempCelsius)
        self.lblCelSign = Label(self.frmCelsius, font=('Roboto', 16), text='\N{DEGREE SIGN}C')

        """Pack the widgets for the frmCelsius frame."""
        self.lblCelSign.pack(side=RIGHT, ipadx=3, ipady=3)
        self.lblCelsius.pack(side=RIGHT, )
        

        """Create the widgets for the frmFahrenheit frame"""
        self.tempFahrenheit = StringVar()
        self.lblFahrenheit = Label(self.frmFahrenheit, font=('Roboto', 16), textvariable=self.tempFahrenheit)
        self.lblFahSign = Label(self.frmFahrenheit, font=('Roboto', 16), text='\N{DEGREE SIGN}F')

        """Pack the widgets for the frmFahrenheit frame."""
        self.lblFahSign.pack(side=RIGHT, ipadx=3, ipady=3)
        self.lblFahrenheit.pack(side=RIGHT)
        
        """Create the widgets for the frmKelvin frame"""
        self.tempKelvin = StringVar()
        self.lblKelvin = Label(self.frmKelvin, font=('Roboto', 16), textvariable=self.tempKelvin)
        self.lblKelSign = Label(self.frmKelvin, font=('Roboto', 16), text='\N{DEGREE SIGN}K')

        """Pack the widgets for the frmKelvin frame."""
        self.lblKelSign.pack(side=RIGHT, ipadx=3, ipady=3)
        self.lblKelvin.pack(side=RIGHT)

        """Create the widgets for the frmMessage frame"""
        self.theMessage = StringVar()
        self.lblMessage = Label(self.frmMessage, textvariable=self.theMessage)

        """Pack the widgets for the frmMessage frame."""
        self.lblMessage.pack()

        """Pack the frames"""
        self.frmDataEntry.pack(fill=BOTH, expand=NO)
        self.frmCelsius.pack(fill=BOTH, expand=YES)
        self.frmFahrenheit.pack(fill=BOTH, expand=YES)
        self.frmKelvin.pack(fill=BOTH, expand=YES)
        self.frmMessage.pack(fill=BOTH, expand=YES)

        """Run the application"""
        mainloop()

    def convert(self):
        try:
            """Set messages to be displayed on the frmMessage frame"""
            messageF = "You converted from \N{DEGREE SIGN}Fahrenheit \n Thank You!"
            messageC = "You converted from \N{DEGREE SIGN}Celsius \n Thank You!"
            messageK = "You converted from \N{DEGREE SIGN}Kelvin \n Thank You!"
            warning = "Please pick appropriate sign \n Thank You!"
            temperature = float(self.entInput.get())
            sign = self.value.get()


            if ("\N{DEGREE SIGN}F" == sign):
                """Pass the temperature value as Fahrenheit"""
                self.tempFahrenheit.set(format(temperature,'0.2f'))

                """Convert temperature from Fahrenheit to Celsius"""
                tempC = (5/9)*(temperature-32)
                self.tempCelsius.set(format(tempC,'0.2f'))
                
                """Convert temperature from Fahrenheit to Kelvin"""
                tempK = ((5/9)*(temperature-32)) + 273.15
                self.tempKelvin.set(format(tempK,'0.2f'))

                self.theMessage.set(messageF)

            elif ("\N{DEGREE SIGN}C" == sign):
                """Pass the temperature value as Celsius"""
                self.tempCelsius.set(format(temperature,'0.2f'))

                """
                Convert temperature from Celsius to Fahrenheit
                and display the result
                """
                tempF = (9*temperature/5) + 32
                self.tempFahrenheit.set(format(tempF, '0.2f'))

                # Conver temperature from Celsius to Kelvin
                tempK = temperature + 273.15
                self.tempKelvin.set(format(tempK,'0.2f'))

                self.theMessage.set(messageC)

            elif ("\N{DEGREE SIGN}K" == sign):
                self.tempKelvin.set(format(temperature,'0.2f'))

                tempF = (temperature - 273.15) + 32
                self.tempFahrenheit.set(format(tempF, '0.2f'))

                tempC = temperature - 273.15
                self.tempCelsius.set(format(tempC,'0.2f'))

                self.theMessage.set(messageK)
            else:
                self.theMessage.set(warning)
        except:
            self.theMessage.set("There was problem retrieving that value!")

if __name__ == '__main__':
    TempConverter()