import requests
import json
import os

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self, user = os.environ.get("username"),token = os.environ.get("sheety_token"),project_name="flightFinder",sheet_name="sheet1") -> None:
        self.user = user
        self.project_name = project_name
        self.sheet_name = sheet_name
        self.token = token
        self.get_data()

    def get_data(self):
        get_request = f"https://api.sheety.co/{self.user}/{self.project_name}/{self.sheet_name}"
        header_request = {
            "Authorization": f"Token {self.token}"
        }
        data = requests.get(url=get_request,headers=header_request)
        data.raise_for_status()
        with open("sheet_json.json",'w') as file:
            json.dump(data.json(),file,indent=4)
        
        self.data = data.json()[self.sheet_name]
    
    
    def update_code(self,row_id:int,code):
        put_request=f"https://api.sheety.co/{self.user}/{self.project_name}/{self.sheet_name}/{row_id+1}"
        updated_row = {
            self.sheet_name : {
                "city": self.data[row_id-1]["city"],
                "iataCode": code,
                "lowestPrice": self.data[row_id-1]["lowestPrice"]
            }
        }
        update_request = requests.put(url=put_request,json=updated_row)
        update_request.raise_for_status()