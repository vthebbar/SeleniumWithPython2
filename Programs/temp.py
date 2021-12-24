from selenium import webdriver
from selenium.webdriver.common.by import By

from webdriver_manager.chrome import ChromeDriverManager

opt = webdriver.ChromeOptions()  #   Remember
opt.headless = True  #OR -> opt.add_argument("--headless") #Remember-To get full snapshot need to run in headless mode

driver = webdriver.Chrome(ChromeDriverManager().install(), options=opt) #   Remember
driver.get("https://mail.rediff.com/cgi-bin/login.cgi")

S = lambda x:driver.execute_script('return document.body.parentNode.scroll'+x)  # Remember
driver.set_window_size(S('Width'),S('Height'))   # Remember
driver.find_element(By.TAG_NAME,'body').screenshot("filename.png")