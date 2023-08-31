import requests
import pytest
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("api_key")

def found_temperature(API_KEY: str, CITY: str):
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
    URL = BASE_URL + "q=" + CITY + "&appid=" + API_KEY
    response = requests.get(URL)
    if response.status_code == 200:
        data = response.json()
        main = data['main']
        temperature = main['temp']
        humidity = main['humidity']
        pressure = main['pressure']
        report = data['weather']
        return temperature, humidity, pressure, report[0]['description']
    else:
        return None

@pytest.mark.parametrize("city", ["Lyon", "Toulon"])
def test_found_temperature(city):

    temperature, humidity, pressure, description = found_temperature(API_KEY, city)
    assert temperature is not None
    assert isinstance(temperature, (int, float))
    assert humidity is not None
    assert isinstance(humidity, int)
    assert pressure is not None
    assert isinstance(pressure, int)
    assert description is not None
    assert isinstance(description, str)
