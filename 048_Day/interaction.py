from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

URL = "https://en.wikipedia.org/wiki/Main_Page"

SELECTOR_PATH = "#articlecount > a:nth-child(1)"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)

article_count = driver.find_element(By.CSS_SELECTOR, "#articlecount a:nth-child(1)")
count = article_count.text

search_bar = driver.find_element(By.NAME, value="search")
search_bar.send_keys("Python", Keys.ENTER)

# driver.quit()
