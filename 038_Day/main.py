import requests
import json
import datetime as dt
import os


application_ID = os.environ.get("application_ID")
API_KEY = os.environ.get("API_KEY")

#SHEETY_ENDPOINT_RETRIEVE = "https://api.sheety.co/edbcb2abb5c65babc176ebcde80bfadd/workouts/sheet1"
SHEETY_ENDPOINT_SEND="https://api.sheety.co/edbcb2abb5c65babc176ebcde80bfadd/workouts/sheet1"

endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

header_exercise = {
    "x-app-id": application_ID,
    "x-app-key": API_KEY
}

exercise_params = {
    "query": input("What sort of exercise did you do?"),
    "weight_kg": 82.5,
    "height_cm": 183,
    "age": 26
}


response = requests.post(url=endpoint,json=exercise_params,headers=header_exercise)
response.raise_for_status()

with open("response.json",'w') as file:
    json.dump(response.json(),file,indent=4)

with open("response.json",'r') as file:
    NLmodel = json.load(file)

present = dt.datetime.now()
date_str = present.strftime("%d/%m/%Y")
time_str=present.strftime("%H:%M:%S")

sheety_entry = {
    "sheet1":
        {
            "date": date_str,
            "time": time_str,
            "exercise": NLmodel["exercises"][0]["name"],
            "duration": NLmodel["exercises"][0]["duration_min"],
            "calories": NLmodel["exercises"][0]["nf_calories"],
            "id": NLmodel["exercises"][0]["compendium_code"]
        }
}

sheety_header = {
    "Authorization": f"Basic {os.environ.get('sheety_token')}",
    "Username": "Joseph01234",
    "Password": os.environ.get("sheety_pass")
}

send_data = requests.post(url=SHEETY_ENDPOINT_SEND,json=sheety_entry,headers=sheety_header)






