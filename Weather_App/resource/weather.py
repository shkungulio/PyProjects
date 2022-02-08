import requests
from bs4 import BeautifulSoup

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
        sky_desc = data[1]

        # printing all data
        city = city
        temp = temp
        time = time
        desc = sky_desc

        #print(other_data)
        weather_info = f'\nToday is: {time}\n\nCity: {city.title()}\nTemperature: {temp}\nWeather Condition: {desc}'

    except Exception:
        weather_info = f'\nThere was problem retrieving that value!'

    return weather_info