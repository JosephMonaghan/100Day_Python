

from selenium import webdriver
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import time, os
import random

load_dotenv()

tgt_url = "https://www.linkedin.com/jobs/search/?currentJobId=4000802211&geoId=101174742&keywords=python%20developer&origin=JOB_SEARCH_PAGE_SEARCH_BUTTON&refresh=true"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(tgt_url)

time.sleep(5)
username = os.getenv("email")
password = os.getenv("pass")

try:
    sign_in_button = driver.find_element(By.NAME,value="homepage-basic_home-hero-sign-in-cta")
except:
    try:
        sign_in_button = driver.find_element(By.CLASS_NAME,value="authwall-join-form__form-toggle--bottom")
    except:
        try:
            sign_in_button = driver.find_element(By.CLASS_NAME,value = "sign-in-modal__outlet-btn")
        except:
            try:
                sign_in_button=driver.find_element(By.CLASS_NAME,value="sign-in-form__sign-in-cta")
            except:
                sign_in_button = driver.find_element(By.CLASS_NAME,value = "cta-modal__primary-btn")

sign_in_button.click()
time.sleep(random.randint(5,7))

user_field = driver.find_element(By.NAME,value="session_key")
pass_field = driver.find_element(By.NAME, value = "session_password")
try:
    submit_button = driver.find_element(By.CLASS_NAME,value="btn__primary--large")
except:
    submit_button = driver.find_element(By.CLASS_NAME,value="btn-md")

user_field.send_keys(username)
pass_field.send_keys(password)
driver.execute_script("arguments[0].click();", submit_button)
time.sleep(random.randint(5,7))
driver.get(tgt_url)
time.sleep(random.randint(5,7))

jobs = driver.find_elements(By.CLASS_NAME,value="job-card-container")
if len(jobs)==0:
    jobs = driver.find_elements(By.CLASS_NAME,value="jobs-search-results__list-item")
if len(jobs)==0:
    jobs = driver.find_elements(By.CLASS_NAME,value="job-card-container--clickable")
print(len(jobs))
for i in range(5):
    job = jobs[i]
    time.sleep(random.randint(4,10)/10)
    driver.execute_script("arguments[0].click();", job)
    time.sleep(random.randint(4,10)/10)
    save_button = driver.find_element(By.CLASS_NAME,value="jobs-save-button")
    save_button.click()

driver.quit()



