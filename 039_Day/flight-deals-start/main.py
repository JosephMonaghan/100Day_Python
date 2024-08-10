#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

from data_manager import DataManager
from flight_search import FlightSearch
from dotenv import load_dotenv
import os
import requests
import json

load_dotenv()

data_manager = DataManager(token=os.getenv("sheety_token"),user=os.getenv("username"))
flight_search = FlightSearch()

iter=0
for destination in data_manager.data:
    iter+=1
    if destination["iataCode"] == "":
        code = flight_search.find_iata(destination["city"])
        destination["iataCode"] = code
        data_manager.update_code(row_id=iter,code=code)





flight_url = "Base URL: test.api.amadeus.com/v1"
dates_url = f"{flight_url}/shopping/flight-dates"

flight_apikey = "AeWZBr78ZAKp5zrQTEKvLZB5q1hNfM7y"
flight_apisecret = "GE1DWCtMwNlksytV"

date_params = {
    "origin": "YVR",
    "destination": "LAS",
    "departureDate": "2024-10-01,2024-12-31", #YYYY-MM-DD format, e.g. 2017-12-25. Ranges are specified with a comma and are inclusive
    "duration": "4,8"
}


