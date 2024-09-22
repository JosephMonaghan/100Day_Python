import requests
from bs4 import BeautifulSoup
import smtplib
from dotenv import load_dotenv
import os

load_dotenv()

URL = "https://appbrewery.github.io/instant_pot/"
live_URL = "https://www.amazon.ca/Instant-Electric-Pressure-Sterilizer-Stainless/dp/B00FLYWNYQ/"
sockets = "https://www.amazon.ca/AmazonBasics-Mechanics-Socket-Set-145-Piece/dp/B074MH432L/"

tgt_URL = URL

headers_amzn = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.4.1 Safari/605.1.15",
    "Accept-Language": "en-CA,en-US;q=0.9,en;q=0.8" 
}

request = requests.get(url=tgt_URL, headers=headers_amzn)
request.raise_for_status()

soup = BeautifulSoup(request.text, 'html.parser')

price_whole = soup.find("span", class_="a-price-whole")
price_fraction = soup.find("span", class_="a-price-fraction")

pdt_title = soup.find("span", {"id": "productTitle"})
pdt_title = pdt_title.text.split("\r")[0]

price = int(price_whole.text.split(".")[0]) + int(price_fraction.text) / 100

if price < 100:
    email_url = "smtp.gmail.com"

    message = f"{pdt_title} available at amazon for {price}:\n{tgt_URL}"

    with smtplib.SMTP(email_url) as connection:
        connection.starttls()
        connection.login(user=os.getenv("email"), password=os.getenv("email_app_passcode"))
        connection.sendmail(from_addr=os.getenv("email"), to_addrs=os.getenv("to_address"), msg=f"Subject: #Amazon Deal! \n\n{message}")

