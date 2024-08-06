import requests
from config import WEATHER_API_KEY

def get_weather():
    weather_url = f"http://api.openweathermap.org/data/2.5/weather?q=YOUR_CITY&appid={WEATHER_API_KEY}"
    response = requests.get(weather_url)
    weather_info = response.json()
    description = weather_info['weather'][0]['description']
    return f"The weather is currently {description}."