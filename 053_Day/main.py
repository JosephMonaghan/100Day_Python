

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
import time, os
import random
import requests
from bs4 import BeautifulSoup
import math

load_dotenv()

tgt_URL = "https://appbrewery.github.io/Zillow-Clone/"
form_URL = "https://docs.google.com/forms/d/e/1FAIpQLSeDYfEhhIcz-dCsoehLuhmztFEpEtAzhhhMZEDNdWb0lEii2Q/viewform?usp=sf_link"

request = requests.get(url=tgt_URL)
request.raise_for_status()

soup = BeautifulSoup(request.text, "html.parser")

# {"class":"presentation"}
listings = soup.find_all("article")

addresses = []
prices = []
links = []


def extract_int(input_str):
    acceptable = "0123456789"
    input_list = [char for char in input_str if char in acceptable]
    return int("".join(input_list))


for listing in listings:
    links.append(listing.find("a")["href"])
    addresses.append(listing.find("address").text.strip())
    price = listing.find("span").text.strip()
    price = extract_int(price)
    if price > 10000:
        price = math.floor(price / 10)
        price = int(price)
    prices.append(price)

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(form_URL)

for listing in range(len(listings)):
    WebDriverWait(driver, 99).until(EC.presence_of_element_located((By.CLASS_NAME, "whsOnd")))

    address_field = driver.find_element(By.CLASS_NAME, "whsOnd")
    address_field.send_keys(addresses[listing], Keys.TAB, str(prices[listing]), Keys.TAB, links[listing])

    submit_button = driver.find_element(By.CLASS_NAME, "NPEfkd")
    submit_button.click()

    WebDriverWait(driver, 99).until(EC.presence_of_element_located((By.LINK_TEXT, "Submit another response")))
    submit_another_link = driver.find_element(By.LINK_TEXT, "Submit another response")
    submit_another_link.click()

driver.quit()
