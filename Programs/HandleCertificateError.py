import time

from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# method 1
opt = Options()

# method 1.1
#opt.add_argument("--ignore-certificate-errors")

# method 1.2
opt.set_capability("acceptInsecureCerts", True)

# method 2
dc= DesiredCapabilities().CHROME.copy()
dc["acceptInsecureCerts"] = True

# method 1, 1.1
driver = webdriver.Chrome(ChromeDriverManager().install(),options=opt)

# Method 2
#driver = webdriver.Chrome(ChromeDriverManager().install(), desired_capabilities=dc)
driver.maximize_window()
driver.get("https://expired.badssl.com/")
driver.implicitly_wait(5)

time.sleep(4)
driver.close()