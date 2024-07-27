import requests
import datetime as dt
import smtplib
import time

my_coords = (49.1659, -123.9401)

def within_range(target_coords):
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    latitude = float(data["iss_position"]["latitude"])
    longitude = float(data["iss_position"]["longitude"])

    return abs(latitude - target_coords[0]) < 5 and abs(longitude - target_coords[1]) < 5



def is_nighttime():
    global my_coords
    parameters = {
        "lat": my_coords[0],
        "lng": my_coords[1],
        "tzid": "America/Vancouver",
        "formatted": 0
    }
    sunrise_response = requests.get(url="https://api.sunrise-sunset.org/json",params=parameters)
    sunrise_response.raise_for_status()
    sunrise = int(sunrise_response.json()["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(sunrise_response.json()["results"]["sunset"].split("T")[1].split(":")[0])

    present = dt.datetime.now()

    return present.hour >= sunset or present.hour <= sunrise

def send_email():
    email = "JM.Python.Learn@gmail.com"
    app_passcode ="lnvq tenb dvxx darv"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=email,password=app_passcode)
        connection.sendmail(from_addr=email,
                            to_addrs="Joseph_Monaghan@outlook.com",
                            msg=f"Subject: Look up!\n\n The ISS should be visible right now!")


while True:
    time.sleep(60)
    if is_nighttime() and within_range(my_coords):
        send_email()