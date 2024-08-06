import requests

def get_time(city):
    time_url = f"http://worldtimeapi.org/api/timezone/{city}"
    response = requests.get(time_url)
    time_info = response.json()
    datetime = time_info['datetime']
    return f"The current time in {city} is {datetime}."