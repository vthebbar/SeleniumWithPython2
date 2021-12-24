# Handle alerts and Handle value key into alert box
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.maximize_window()
driver.find_element(By.XPATH,"//button[text()='Click for JS Prompt']").click()
alert = driver.switch_to.alert
print(alert.text)
alert.send_keys("Hi")
time.sleep(2)
alert.accept()
time.sleep(2)

driver.find_element(By.XPATH,"//button[text()='Click for JS Confirm']").click()
a1=driver.switch_to.alert
print(a1.text)
time.sleep(2)
a1.accept()
time.sleep(2)

driver.find_element(By.XPATH,"//button[text()='Click for JS Alert']").click()
a2=driver.switch_to.alert
print(a2.text)
time.sleep(2)
a2.accept()
time.sleep(2)

driver.quit()