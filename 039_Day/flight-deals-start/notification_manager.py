import os
from dotenv import load_dotenv
import smtplib


load_dotenv()

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self) -> None:
        self.user = os.getenv("email")
        self.password = os.getenv("email_passcode")
        self.target = os.getenv("target_email")
    
    def compose_message(self,city_data,price_list):
        message = "Subject: Your Flight Report\n\n"
        iter=-1
        for entry in city_data:
            iter+=1
            if price_list[iter] == -1 or price_list[iter] == 99999.0:
                add_message = f'{entry["city"]}: no flights available\n'
            else:
                add_message = f'{entry["city"]}: {price_list[iter]} CAD\n'
            
            message += add_message
        
        return message
            

    def send_message(self,message):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=self.user,password=self.password)
            connection.sendmail(from_addr=self.user,to_addrs=self.target,msg=message)
        