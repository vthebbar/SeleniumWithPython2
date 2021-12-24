# Drag and drop
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://jqueryui.com/droppable/")
driver.maximize_window()
driver.switch_to.frame(0)
src = driver.find_element(By.ID,'draggable')
tgt = driver.find_element(By.ID,'droppable')

action = ActionChains(driver)
#action.drag_and_drop(src,tgt).perform()  # perform is required


# multiple actions(2nd approach -  > click and hold, move to element and release)
action.click_and_hold(src).move_to_element(tgt).release().perform()

time.sleep(5)
driver.quit()