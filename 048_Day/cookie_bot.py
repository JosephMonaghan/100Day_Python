from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

URL = "https://orteil.dashnet.org/cookieclicker/"

eng_selector = "#langSelect-EN"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)

time.sleep(15)
english_select = driver.find_element(By.CSS_SELECTOR, eng_selector)
english_select.click()

time.sleep(15)
# driver.find_element(By.XPATH, "//button[text()='Accept All']").click()
cookie = driver.find_element(By.ID, "bigCookie")
my_cookies = driver.find_element(By.ID, "cookies").text


def click_element(self, element):
    self.driver.execute_script("arguments[0].click();", element)


start_time = time.time()
time_now = time.time()
elapsed_time = time_now - start_time
while elapsed_time < 300:
    click_time = time.time()
    time_now = time.time()
    click_elapsed = time_now - click_time
    while click_elapsed < 5:
        cookie.click()
        click_elapsed = time.time() - click_time

    pdts = driver.find_elements(By.CSS_SELECTOR, "span.price")
    prices = []
    my_cookies = int(driver.find_element(By.ID, "cookies").text.split(" ")[0])
    for pdt in pdts[::-1]:
        if pdt.text != "":
            price_str = pdt.text
            price_str = price_str.replace(",", "")
            price_val = int(price_str)
            while price_val < my_cookies:
                driver.execute_script("arguments[0].click();", pdt)
                my_cookies = int(driver.find_element(By.ID, "cookies").text.split(" ")[0])
    
    elapsed_time = time.time() - start_time
    print(elapsed_time)

print("Finished!")

