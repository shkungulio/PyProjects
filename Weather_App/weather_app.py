"""This app will search weather by city and return the city name; current day, date, and time; temperature; and weather condition.
This app uses tkinter to create graphical user interface (GUI) """
from tkinter import *
from tkinter.font import Font
from bs4 import BeautifulSoup
import requests

HEIGHT = 400
WIDTH = 600

root = Tk()
root.title("Weather Application")
root.resizable(False, False)
root.iconbitmap('weather.ico')

def searchWeather(city):
    try:
        # creating url and requests instance
        url = "https://www.google.com/search?q="+"weather"+city
        html = requests.get(url).content
        
        # getting raw data
        soup = BeautifulSoup(html, 'html.parser')
        temp = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text
        str = soup.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text
        
        # formatting data
        data = str.split('\n')
        time = data[0]
        sky = data[1]
        
        # getting all div tag
        listdiv = soup.findAll('div', attrs={'class': 'BNeawe s3v9rd AP7Wnd'})
        strd = listdiv[5].text
        
        
        # getting other required data
        pos = strd.find('Wind')
        other_data = strd[pos:]
        

        # printing all data
        city = city
        temp = temp
        time = time
        desc = sky
        #print(other_data)
        lblMain['text'] = 'Today is: ' + time + '\n\nCity: ' + city + '\nTemperature: ' + temp + '\nWeather Condition: ' + desc

    except:

        lblMain['text'] = "There was problem retrieving that value!"

    
"""
create canvas that will define the length and width of the app 
and the background image
"""
canvas = Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack(pady=5, padx=5)

bgImage = PhotoImage(file="./weather.png")
bgLabel = Label(root, image=bgImage)
bgLabel.place(relwidth=1)

"""
create a frame to hold an input entry and button that will 
allow to enter a city and search weather information
"""
frmFirst = Frame(bgLabel, bg='#7F9200', border=5)
frmFirst.place(relx=0.5, rely=0.1, relwidth=0.8, relheight=0.1, anchor="n")

entInput = Entry(frmFirst, font=50)
entInput.place(relwidth=0.65, relheight=1)
btnInput = Button(frmFirst, text="Search", font=50, command=lambda: searchWeather(entInput.get()))
btnInput.place(relx=0.67, relwidth=0.33, relheight=1)

"""
create a frame to hold a label that will display weather information
"""
frmSecond = Frame(bgLabel, bg='#7F9200', border=5)
frmSecond.place(relx=0.5, rely=0.35, relwidth=0.8, relheight=0.5, anchor='n')

"""
create a label to display the weather information
"""
lblMain = Label(frmSecond, font=('Arial',16), anchor='nw', justify=LEFT)
lblMain.place(relwidth=1, relheight=1)

"""
create a label to display copyright information
"""
lblMsg = Label(root, text='\N{COPYRIGHT SIGN} 2021 | shkungulio | All rights reserved')
lblMsg.pack()

""" run the application """
root.mainloop()