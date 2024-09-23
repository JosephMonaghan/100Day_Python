from selenium import webdriver
from selenium.webdriver.common.by import By

URL = "https://www.python.org"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)

# price_whole = driver.find_element(By.CLASS_NAME, value="a-price-whole").text
# price_fractional = driver.find_element(By.CLASS_NAME, value="a-price-fraction").text

# print(price_whole, price_fractional)

date_list = driver.find_elements(By.CSS_SELECTOR, "div.event-widget li")

event_dict = {}

iter = -1
for date in date_list:
    iter += 1
    print(date.text.split("\n"))
    event_date = date.text.split("\n")[0]
    event_name = date.text.split("\n")[1]

    event_dict[iter] = {"time": event_date, "name": event_name}

print(event_dict)
driver.quit()
