# rain-alert
SMS alert app for bad weathers.

## Table of Contents
* [General Info](#general-info)
* [Built With](#built-with)
* [Environment Variables](#environment-variables)
* [Open Weather Map Parameters](#open-weather-map-parameters)

## General Info
This project is a simple alert app for bad weathers which we need an umbrella.<br />
Weather data retrieved from Open Weather Map API.<br />
Twilio used for sending alert sms to users.<br />

## Built With
Project is created with:
* Python version: 3.10
* requests version: 2.28.1
* twilio version: 7.14.0

## Environment Variables
I used environment variables for API keys and some personal information for security reasons. You should change this parts of code with your information.
```
# TWILIO VARIABLES
account_sid = os.environ.get("TWILIO_SID")
auth_token = os.environ.get("TWILIO_TOKEN")
FROM_NUM = os.environ.get("TWILIO_FROM")
TO_NUM = os.environ.get("TWILIO_TO")

# OWM VARIABLES
OWM_API_KEY = os.environ.get("OWM_API_KEY")
```

## Open Weather Map Parameters
You can change lat(latitude) and lon(longitude) variables with your locations values. I used currently rainy location for testing.<br />

```
PARAMETERS = {
    "lat": 45.815010,
    "lon": 15.981919,
    "exclude": "current,minutely,daily",
    "appid": OWM_API_KEY,
}
```
