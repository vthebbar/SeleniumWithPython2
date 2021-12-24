# To get all links in a web page and print link text and URL

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

import Config.Config as cfg

if cfg.Browser == "Chrome":
    driver = webdriver.Chrome(ChromeDriverManager().install())
else:
    raise Exception("Browser Name Invalid or Browser not supported")

driver.maximize_window()
driver.get("https://frontend.nopcommerce.com/")
driver.implicitly_wait(2)

links1 = driver.find_elements(By.TAG_NAME,'a')
for l in links1:
    print("Link Text=", l.text, "Link URL=", l.get_attribute('href'))

driver.switch_to.frame(0)     # Need to switch to correct frame , else result will be unexpected

links2 = driver.find_elements(By.TAG_NAME,'a')
links = links1 + links2

for l in links2:
    print("Link text=",l.text," Link URL=",l.get_attribute('href'))

print("Total Number of links=", len(links))