# Use of ActionChains class
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://classic.crmpro.com/index.html")
driver.maximize_window()
driver.implicitly_wait(5)

id = driver.find_element(By.NAME,'username')
pwd = driver.find_element(By.NAME,'password')
loginbtn = driver.find_element(By.XPATH,"//input[@type='submit']")

action = ActionChains(driver)
action.send_keys_to_element(id,'raja')    # do not use .perform() with send_keys_to_element
action.send_keys_to_element(pwd,'pwd')    # do not use .perform() with send_keys_to_element
time.sleep(2)
action.click(loginbtn).perform()
time.sleep(2)

driver.quit()