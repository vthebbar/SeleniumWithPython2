# Right click or content click
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")
driver.maximize_window()

element = driver.find_element(By.XPATH,"//span[text()='right click me']")
action = ActionChains(driver)
action.context_click(element).perform()  # perform is must

# Get options after right click
opt = driver.find_elements(By.CSS_SELECTOR,'ul li span')
print(len(opt))

for o in opt:
    print(o.text)
    if o.text == "Quit":
        o.click()
        break

driver.switch_to.alert.accept()
driver.switch_to.default_content()

time.sleep(4)
driver.quit()