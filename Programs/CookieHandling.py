# Cookie handling

from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.screener.in/")
driver.maximize_window()
driver.implicitly_wait(10)
cookies=driver.get_cookies()
print(cookies)
print(type(cookies))  # list
driver.add_cookie({"name" : "vishwa","ID":"ID123", "value":"1234"}) #value attribute is must
print("****************************")
cookies=driver.get_cookies()
print(cookies)

for c in cookies:
    print(c.values())
    print(c.keys())