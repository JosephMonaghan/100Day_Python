import os
from dotenv import load_dotenv
import requests
import datetime
import json

load_dotenv()

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    pass
    def __init__(self) -> None:
        self._api_key=os.getenv("flight_apikey")
        self._api_secret=os.getenv("flight_apisecret")
        self._token=self.get_new_token()


    def find_iata(self,city: str):
        endpoint = "https://test.api.amadeus.com/v1/reference-data/locations/cities"

        send_header = {
            "Authorization": f"Bearer {self._token}"
        }

        send_data = {
            "keyword": city
        }
        response = requests.get(url=endpoint,headers=send_header,params=send_data)
        response.raise_for_status()
        return response.json()['data'][0]['iataCode']


    
    def get_new_token(self):
        endpoint = "https://test.api.amadeus.com/v1/security/oauth2/token"
        send_json = {
            "grant_type": "client_credentials",
            "client_id": self._api_key,
            "client_secret": self._api_secret,
        }

        send_header = {
            "Content-Type": "application/x-www-form-urlencoded"
        }

        response = requests.post(url=endpoint,data=send_json,headers=send_header)
        response.raise_for_status()
        data = response.json()
        return data["access_token"]
    
    def get_price(self,origin,destination):
        present =datetime.datetime.now()
        day_after_tmr = present + datetime.timedelta(days=2)
        end_date = present + datetime.timedelta(days=20)


        endpoint = "https://test.api.amadeus.com/v2/shopping/flight-offers"
        send_header = {
            "Authorization": f"Bearer {self._token}"
        }
        params_flight = {
            "originLocationCode": origin,
            "destinationLocationCode": destination,
            "departureDate": day_after_tmr.strftime("%Y-%m-%d"),
            "returnDate": end_date.strftime("%Y-%m-%d"),
            "adults": 1,
            "currencyCode": "CAD",
            "max": 5
        }

        request = requests.get(url=endpoint,headers=send_header,params=params_flight)
        request.raise_for_status()
        try:
            return self.find_lowest_price(request.json()['data'])
        except:
            return -1


    def find_lowest_price(self,data):
        lowest_offer = float(99999)
        for offer in data:
            if float(offer["price"]["total"]) < lowest_offer:
                lowest_offer = float(offer["price"]["total"])
        
        return lowest_offer


        
    
    