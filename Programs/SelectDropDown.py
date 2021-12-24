# Select dropdown
# Use Generic function for item selection from select drop down

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.opera import OperaDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.microsoft import IEDriverManager

import Config.Config as cfg

if cfg.Browser == "Chrome":
    driver = webdriver.Chrome(ChromeDriverManager().install())
elif cfg.Browser == "Firefox":
    driver = webdriver.Firefox(executable_path = GeckoDriverManager().install())
elif cfg.Browser == "Opera":
    driver = webdriver.Opera(executable_path=OperaDriverManager().install())
elif cfg.Browser == "MSEdge":
    #driver = webdriver.Edge(EdgeChromiumDriverManager().install())
    driver = webdriver.Edge(executable_path=cfg.MSEdgeDriver_path)
elif cfg.Browser == "IE":
    #driver = webdriver.Ie(IEDriverManager().install())
    driver = webdriver.Ie(executable_path=cfg.IEDriver_path)
else:
    raise Exception("Invalid browser name or browser not supported")

# Generic Function for select dropdown item selection
def select_from_dropdown(element, value):
    select = Select(element)
    select.select_by_visible_text(value)


# Accessing elements
driver.maximize_window()
driver.get("https://frontend.nopcommerce.com/")
driver.switch_to.frame(0)
driver.find_element(By.LINK_TEXT,'Register').click()

day = driver.find_element(By.NAME,'DateOfBirthDay')
select_from_dropdown(day,"1")

month = driver.find_element(By.NAME,'DateOfBirthMonth')
select_from_dropdown(month,"January")

year = driver.find_element(By.NAME,'DateOfBirthYear')
select_from_dropdown(year,"2002")
