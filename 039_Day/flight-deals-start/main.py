#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

from data_manager import DataManager
from flight_search import FlightSearch
from dotenv import load_dotenv
from notification_manager import NotificationManager
import os
import time


load_dotenv()

data_manager = DataManager(token=os.getenv("sheety_token"),user=os.getenv("username"))
flight_search = FlightSearch()
notification_manager = NotificationManager()

iter=0
price_list=[]
for destination in data_manager.data:
    iter+=1
    if destination["iataCode"] == "":
        code = flight_search.find_iata(destination["city"])
        destination["iataCode"] = code
        data_manager.update_code(row_id=iter,code=code)

    origin = "YVR"

    dest_price = flight_search.get_price(origin=origin,destination=destination["iataCode"])
    time.sleep(3)
    price_list.append(dest_price)


msg = notification_manager.compose_message(city_data=data_manager.data,price_list=price_list)
print(msg)
notification_manager.send_message(message=msg)

