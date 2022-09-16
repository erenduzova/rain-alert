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
next_12_data = weather_data["hourly"][:12]

will_rain = False
for hour_d in next_12_data:
    if int(hour_d["weather"][0]["id"]) < 700:
        will_rain = True

if will_rain:
    print("It's going to rain today. Remember to bring an ☂️")
