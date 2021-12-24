# To get total number of images in a web page and print the image attributes

from selenium import webdriver
from selenium.webdriver.common.by import By

from webdriver_manager.chrome import ChromeDriverManager

import Config.Config as cfg

if cfg.Browser == "Chrome":
    driver = webdriver.Chrome(ChromeDriverManager().install())
else:
    raise Exception("Invalid browser name or browser not supported")

driver.maximize_window()
driver.get("https://frontend.nopcommerce.com/")

images1 = driver.find_elements(By.TAG_NAME,'img')
print(len(images1))

for i in images1:
    alt = i.get_attribute('alt')
    src = i.get_attribute('src')
    print("Alt=", alt, "Src=", src)

driver.switch_to.frame(0)

images2 = driver.find_elements(By.TAG_NAME,'img')
print(len(images2))

for i in images2:
    alt=i.get_attribute('alt')
    src=i.get_attribute('src')
    print("Alt=", alt, "Src=", src)

total_image_tags = len(images1)+len(images2)
print("Total images",total_image_tags)