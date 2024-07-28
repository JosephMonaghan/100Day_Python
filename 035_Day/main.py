import requests
import smtplib
import os

email = "JM.Python.Learn@gmail.com"
app_passcode ="lnvq tenb dvxx darv"


target_email = "trevorandrews123@gmail.com"



params_call = {
    "lat" : 49.1659,
    "lon" : -123.9401,
    "appid" : "cefd7cb95989f993ec9a293dedb1c750",
    "units" : "metric",
    "cnt" : 4,
    }
   
response = requests.get(url="http://api.openweathermap.org/data/2.5/forecast?",params=params_call)
response.raise_for_status()

data = response.json()["list"]
count = response.json()["cnt"]

will_rain = False
for forecast in data:
    id = forecast['weather'][0]['id']
    if id < 700:
        will_rain = True
        break


with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=email, password=app_passcode)

    if will_rain:
        connection.sendmail(from_addr=email,
                            to_addrs=target_email,
                            msg="Subject: Rain Today!\n\n Pack an umbrella!")
    else:
        connection.sendmail(from_addr=email,
                            to_addrs=target_email,
                            msg="Subject: Dry Today!\n\n Suns out guns out!")