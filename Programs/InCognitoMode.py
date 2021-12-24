# Run browser in incognito mode
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from webdriver_manager.chrome import ChromeDriverManager

option = webdriver.ChromeOptions()
option.add_argument("--incognito")

driver = webdriver.Chrome(ChromeDriverManager().install(), options=option)
driver.get("https://google.com")
driver.maximize_window()
time.sleep(4)

driver.quit()