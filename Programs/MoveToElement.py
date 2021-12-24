# Move to element
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common import actions
from webdriver_manager.chrome import ChromeDriverManager
import time
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.vthwealth.com/2020/03/recurring-deposit.html")
driver.maximize_window()
driver.implicitly_wait(2)


time.sleep(2)
#driver.switch_to.frame(1)
save = driver.find_element(By.XPATH,"//*[@id='cssnav']/li[1]/a")
current = driver.find_element(By.XPATH,'//*[@id="cssnav"]/li[1]/ul/li[2]/a')

action = ActionChains(driver)
action.move_to_element(save).move_to_element(current).perform()
current.click()
time.sleep(2)

driver.quit()

