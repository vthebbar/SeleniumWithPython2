# Execute Javascript using selenium
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://yahoo.com")
driver.maximize_window()
time.sleep(1)
# Refresh the page
driver.execute_script("history.go(0)")
time.sleep(1)

# Get page title
title = driver.execute_script("return document.title")
print(title)

# click on element
element = driver.find_element(By.XPATH,"//span[text()='Mail']")
driver.execute_script("arguments[0].click()",element)
time.sleep(1)

# scroll down to bottom of page

driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
time.sleep(1)

# Get inner text of web page
text = driver.execute_script("return document.documentElement.innerText")
print(text)

driver.get("https://amazon.in")
driver.maximize_window()

wait = WebDriverWait(driver,10)
wait.until(ec.visibility_of_element_located((By.XPATH,
                                    "//span[text()='Best Sellers in Books']")))

ele=driver.find_element(By.XPATH,"//span[text()='Best Sellers in Books']")

# scroll to a particular element
driver.execute_script("arguments[0].scrollIntoView(true)",ele)   # important

time.sleep(4)

# Generate alert message
driver.get("https://google.com")
driver.execute_script("alert('Alert generated - selenium - python')")

time.sleep(2)
alert = driver.switch_to.alert
alert.accept()
time.sleep(2)

info = driver.execute_script("return navigator.userAgent")
print(info)

driver.close()