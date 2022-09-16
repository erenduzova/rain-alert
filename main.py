import requests
import os

OWM_API_KEY = os.environ.get("OWM_API_KEY")
PARAMETERS = {
    "lat": 45.815010,
    "lon": 15.981919,
    "exclude": "current,minutely,daily",
    "appid": OWM_API_KEY,
}
OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"

response = requests.get(url=OWM_ENDPOINT, params=PARAMETERS)
response.raise_for_status()
weather_data = response.json()

print(weather_data)
