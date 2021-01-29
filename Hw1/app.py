from urllib import parse
from flask import Flask,render_template,request

import requests


from urllib.parse import quote
from urllib.request import urlopen
import json

import socket

app = Flask(__name__)

WEATHER_URL = "http://api.openweathermap.org/data/2.5/weather?q={0}&units=metric&APPID={1}"
WEATHER_KEY = '0ddfcdaf5b6e6101eb6c6bc65810ef7d'

NEWS_URL = "https://newsapi.org/v2/top-headlines?q={0}&apiKey={1}"
NEWS_KEY = '50b07b77004c4764b1eff0fa2fa09283'

@app.route('/')
@app.route('/index')
def index():
    city = request.args.get('city')

    if not city:
        res = requests.get('https://ipinfo.io/')
        city = res.json()['city']
    
    news = getCovidNews()

    weather = get_weather(city,WEATHER_KEY)
    return render_template('index.html',weather=weather,news=news)


@app.route('/news')
def news():
    tag = request.args.get('search_news')

    if not tag:
        tag = 'tesla'

    news = searchNews(tag,NEWS_KEY)
    return render_template('news.html', news=news)



@app.route('/aboutme')
def aboutme():
    return render_template('aboutme.html')

def searchNews(tag,API_KEY):
    query = quote(tag)
    url = NEWS_URL.format(query, API_KEY)
    print(url)
    data = urlopen(url).read()
    parsed = json.loads(data)
    news = parsed.get('articles')
    
    return news
    

    
def getCovidNews():
    url = "https://newsapi.org/v2/top-headlines?q=covid&page=1&apiKey=50b07b77004c4764b1eff0fa2fa09283"
    res = requests.get(url)
    news = res.json()
    list_news = list()
    
    for i in range(0,5):
        list_news.append(news['articles'][i])
    
    return list_news




def get_weather(city,API_KEY):
    query = quote(city)
    print(query)
    url = WEATHER_URL.format(query, API_KEY)
    print(url)
    data = urlopen(url).read()
    parsed = json.loads(data)
    weather = None

    if parsed.get('weather'):

        description = parsed['weather'][0]['description']
        temperature = parsed['main']['temp']
        city = parsed['name']
        icon = parsed['weather'][0]['icon']
        country = parsed['sys']['country']
        wind = parsed['wind']['speed']
        humidity = parsed['main']['humidity']
        pressure = parsed['main']['pressure']
        
        weather = {'description': description,
                    'temperature': temperature,
                    'city': city,
                    'country': country,
                    'icon': icon,
                    'wind': wind,
                    'humidity': humidity,
                    'pressure': pressure
                    }

    return weather



if __name__ == '__main__':
    app.run(debug=True,use_reloader=True)