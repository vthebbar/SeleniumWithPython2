# Headless browser testing using firefox

from selenium import webdriver
from selenium.webdriver.common.by import By

from webdriver_manager.firefox import GeckoDriverManager

option = webdriver.FirefoxOptions()
option.add_argument("--headless")

driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(),options=option)
driver.get("https://google.com")
print(driver.title)

page_text = driver.execute_script("return document.documentElement.innerText;")
print(page_text)