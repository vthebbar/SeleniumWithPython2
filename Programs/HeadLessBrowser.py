# Headless browser test for chrome

from selenium import webdriver
from selenium.webdriver.common.by import By

from webdriver_manager.chrome import ChromeDriverManager

option = webdriver.ChromeOptions()
option.add_argument("--headless")

driver = webdriver.Chrome(ChromeDriverManager().install(),options=option)
driver.get("https://google.com")
print(driver.title)
text = driver.execute_script("return document.documentElement.innerText;")
print(text)

