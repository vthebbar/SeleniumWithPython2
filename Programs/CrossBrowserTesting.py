# Open Google in multiple browsers and perform google search and verify if a particular value is found or not

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.microsoft import IEDriverManager
from webdriver_manager.opera import OperaDriverManager


import Config.Config as cfg
import time

if cfg.Browser == "Chrome":
    driver = webdriver.Chrome(ChromeDriverManager().install())
elif cfg.Browser == "Firefox":
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
elif cfg.Browser == "MSEdge":
    #driver = webdriver.Edge(EdgeChromiumDriverManager().install())
    driver = webdriver.Edge(executable_path=cfg.MSEdgeDriver_path)
elif cfg.Browser == "IE":
    #driver = webdriver.Ie(IEDriverManager().install())
    driver = webdriver.Ie(executable_path=cfg.IEDriver_path)
elif cfg.Browser == "Opera":
    driver = webdriver.Opera(executable_path=OperaDriverManager().install())
else:
    raise Exception("Invalid Browser Name or Browser not supported")

driver.maximize_window()
driver.get("https://google.com")
driver.implicitly_wait(2)

search_textbox = driver.find_element(By.NAME,'q')
search_textbox.send_keys("Python")

search_opt_list = driver.find_elements(By.CSS_SELECTOR,'ul.G43f7e li span')
print(len(search_opt_list))

flag=0
for ele in search_opt_list:
    print(ele.text)
    if ele.text == "Python Tutorial":
        flag = 1
        print("Found - Python Tutorial")
        break
if flag == 0:
    print("Not found - Python Tutorial")

driver.close()
