import requests
from twilio.rest import Client

### WEATHER API ###
###################

api_key = "ad39c8ebdfc4fef1e1fd0432dd5df961"
end_point = "https://api.openweathermap.org/data/2.5/forecast"
parameters = {
    'lat'  : 42.653810,
    'lon'  : 23.314759,
    'units': 'metric',
    'appid': api_key
}

response = requests.get(url=end_point, params=parameters)
weather_data = response.json()

###  TWILIO API ###
###################
def sms_sender():
    account_sid = "AC72dd09fb5fc1ed43f5eac0e029598255"
    auth_token = "c1a8303105fc7dcc124aa0c4045297e8"

    client = Client(account_sid, auth_token)
    message  = client.messages.create(
                    body="It's going to rain today. Bring an umbrella!",
                    from_="+19843558644",
                    to="+359 87 746 1444"
                )
    return print(message.status)

### PROGRAM ###
###############

number_of_forecasts = 4
will_rain = False
for hour_index in range(number_of_forecasts):
    weather_dt = weather_data['list'][hour_index]['dt_txt']
    weather_id = weather_data['list'][hour_index]['weather'][0]['id']
    if int(weather_id) < 600:
        will_rain = True
        rain_dt = weather_dt


if will_rain:
    sms_sender()
    print(rain_dt)
else:
    print("Will not rain")
