# Take screenshot of visible part of web page

from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://yahoo.com")
driver.maximize_window()
driver.implicitly_wait(5)
driver.get_screenshot_as_file("snapshot.png")

driver.quit()
