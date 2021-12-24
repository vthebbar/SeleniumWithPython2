# Select dropdown element selection without using select class
# we can use find elements to achieve this
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

import Config.Config as cfg

if cfg.Browser == "Chrome":
    driver = webdriver.Chrome(ChromeDriverManager().install())
else:
    raise Exception("Invalid Browser name or Browser not supported")

driver.maximize_window()
driver.get("https://frontend.nopcommerce.com/")
driver.switch_to.frame(0)
driver.find_element(By.LINK_TEXT,'Register').click()

# Generic function to select dropdown without using select class
def select_dropdown_option(dropdownOptions,value):
    for ele in dropdownOptions:
        if ele.text == value:
            ele.click()
            break


date_dropdown = driver.find_elements(By.XPATH,"//select[@name='DateOfBirthDay']/option")
print(len(date_dropdown))
select_dropdown_option(date_dropdown,"31")

month_dropdown = driver.find_elements(By.XPATH,"//select[@name='DateOfBirthMonth']/option")
select_dropdown_option(month_dropdown,"December")

year_dropdown = driver.find_elements(By.XPATH,"//select[@name='DateOfBirthYear']/option")
select_dropdown_option(year_dropdown,"2002")

'''
for ele in dropdown_options:
    print(ele.text)
    if ele.text == "31":  # 31 should be within " ", else
        ele.click()
'''

time.sleep(5)


