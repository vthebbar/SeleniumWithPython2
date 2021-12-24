# Use different element locators  and choose from select dropdown

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.opera import OperaDriverManager
from webdriver_manager.microsoft import IEDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

import Config.Config as cfg

import os
import time

if cfg.Browser == "Chrome":
    driver = webdriver.Chrome(ChromeDriverManager().install())
elif cfg.Browser == "Firefox":
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
elif cfg.Browser == "Opera":
    driver = webdriver.Opera(executable_path=OperaDriverManager().install())
elif cfg.Browser == "IE":
    #driver = webdriver.Ie(IEDriverManager().install())
    driver = webdriver.Ie(executable_path=cfg.IEDriver_path)
elif cfg.Browser == "MSEdge":
    #driver = webdriver.Edge(EdgeChromiumDriverManager().install())
    driver = webdriver.Edge(executable_path=cfg.MSEdgeDriver_path)
else:
    raise Exception("Invalid Browser Name or Browser Not supported")

driver.maximize_window()
driver.get("https://frontend.nopcommerce.com/")
driver.implicitly_wait(2)
driver.switch_to.frame(0)
driver.find_element(By.LINK_TEXT,'Register').click()

gender_male = driver.find_element(By.XPATH,"//input[@value='M']")
gender_female = driver.find_element(By.ID,'gender-female')
first_name = driver.find_element(By.NAME,'FirstName')
last_name = driver.find_element(By.ID,'LastName')

day = driver.find_element(By.NAME,'DateOfBirthDay')
select_date = Select(day)
print("IS MULTIPLE?",select_date.is_multiple) # to check whether drop down allows to select multiple values

month = driver.find_element(By.XPATH,"//select[@name='DateOfBirthMonth']")
select_month = Select(month)

year = driver.find_element(By.NAME,'DateOfBirthYear')
select_year = Select(year)

email = driver.find_element(By.XPATH,"//input[@type='email']")
company = driver.find_element(By.ID,'Company')
news_letter_checkbox = driver.find_element(By.ID,'Newsletter')
password = driver.find_element(By.ID,'Password')
confirm_password = driver.find_element(By.ID,'ConfirmPassword')
register_button = driver.find_element(By.ID,'register-button')

gender_male.click()
first_name.send_keys("Raj")
last_name.send_keys("Kumar")

select_date.select_by_visible_text("1")
select_month.select_by_visible_text("January")
select_year.select_by_visible_text("2000")

email.send_keys("raj@gmail.com")
company.send_keys("IT Company")
news_letter_checkbox.click()
password.send_keys("Raj@1234")
confirm_password.send_keys("Raj@1234")
register_button.click()

time.sleep(5)
driver.close()