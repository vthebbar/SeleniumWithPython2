# Take full page screen shot

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

option = webdriver.ChromeOptions()
# option.add_argument("--headless")
option.headless = True

driver = webdriver.Chrome(ChromeDriverManager().install(), options=option)

driver.get("https://yahoo.com")
driver.maximize_window()
driver.implicitly_wait(5)

S = lambda x: driver.execute_script('return document.body.parentNode.scroll'+x)
driver.set_window_size(S('Width') ,S('Height'))
driver.find_element(By.TAG_NAME,'body').screenshot("Fullsnapshot.png")
driver.quit()