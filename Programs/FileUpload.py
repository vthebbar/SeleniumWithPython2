# File Upload
#C:\Users\user\PycharmProjects\SeleniumWithPython2\Files\Uploadfile.txt

import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from webdriver_manager.chrome import ChromeDriverManager
from Config import Config as cfg
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://the-internet.herokuapp.com/upload")
driver.maximize_window()
time.sleep(1)
driver.find_element(By.ID,'file-upload').send_keys(cfg.upload_file_path)
time.sleep(2)
driver.find_element(By.ID,'file-submit').click()

time.sleep(4)
driver.quit()
