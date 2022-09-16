import requests
import os
from twilio.rest import Client

# TWILIO VARIABLES
account_sid = os.environ.get("TWILIO_SID")
auth_token = os.environ.get("TWILIO_TOKEN")
FROM_NUM = os.environ.get("TWILIO_FROM")
TO_NUM = os.environ.get("TWILIO_TO")

# OWM VARIABLES
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
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
            body="It's going to rain today. Remember to bring an ☂️",
            from_=FROM_NUM,
            to=TO_NUM
        )
    print(message.status)
