# Handle certificate error in firefox
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import DesiredCapabilities
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver import FirefoxProfile

# method 1
dc = DesiredCapabilities().FIREFOX.copy()
dc["acceptInsecureCert"] = True

# method 2J
profile = FirefoxProfile()
profile.accept_untrusted_certs = True

#method 1
#driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), desired_capabilities=dc)

# method 2
driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), firefox_profile=profile)

driver.maximize_window()
driver.get("https://expired.badssl.com/")

time.sleep(4)
driver.close()