# To get all values in drop down list

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from webdriver_manager.chrome import ChromeDriverManager
import Config.Config as cfg

if cfg.Browser == "Chrome":
    driver = webdriver.Chrome(ChromeDriverManager().install())
else:
    raise Exception("Invalid Browser name or Browser not supported")

driver.maximize_window()
driver.get("https://frontend.nopcommerce.com/")
driver.switch_to.frame(0)

driver.find_element(By.LINK_TEXT,"Register").click()
driver.implicitly_wait(1)

# function to get values from dropdown list
def get_dropdown_items(dropdownlist):
    select = Select(dropdownlist)
    opt = select.options
    for o in opt:
        print(o.text)

date_dropdown = driver.find_element(By.NAME,'DateOfBirthDay')
get_dropdown_items(date_dropdown)

month_drop_down = driver.find_element(By.NAME,"DateOfBirthMonth")
get_dropdown_items(month_drop_down)

year_drop_down = driver.find_element(By.NAME,"DateOfBirthYear")
get_dropdown_items(year_drop_down)