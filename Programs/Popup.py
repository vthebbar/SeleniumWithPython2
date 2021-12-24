# Authentication pop up
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth") #pass id and password in url
driver.maximize_window()
time.sleep(5)

driver.quit()