from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

FNAME = "Fred"
LNAME = "Mercury"

EMAIL = "FreddyBoi123@Mercury.ca"

URL = "http://secure-retreat-92358.herokuapp.com"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)

# ody > form > input.form - control.top
fname_field = driver.find_element(By.NAME, value="fName")
fname_field.send_keys(FNAME)

lname_field = driver.find_element(By.NAME, value="lName")
lname_field.send_keys(LNAME)

email_field = driver.find_element(By.NAME, "email")
email_field.send_keys(EMAIL, Keys.ENTER)

