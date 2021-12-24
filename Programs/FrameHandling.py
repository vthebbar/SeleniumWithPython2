# Frame handling
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.quackit.com/html/examples/frames/")
driver.maximize_window()
driver.implicitly_wait(2)
time.sleep(1)
driver.switch_to.frame("aswift_0")
driver.find_element(By.CLASS_NAME,'img_ad').click()

time.sleep(5)
driver.quit()