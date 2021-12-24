# Handling pop up alerts

from selenium import webdriver
from selenium.webdriver.common.by import By

from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://mail.rediff.com/cgi-bin/login.cgi")
driver.maximize_window()
driver.implicitly_wait(2)
driver.find_element(By.NAME,'proceed').click()
time.sleep(2)
alert = driver.switch_to.alert
print(alert.text)
alert.accept()
time.sleep(2)

#driver.switch_to.default_content()
driver.find_element(By.ID,'login1').send_keys("userid")
time.sleep(2)
driver.quit()