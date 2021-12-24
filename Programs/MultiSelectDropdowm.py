# Handling multi select jquery/angular js dropdown
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.jqueryscript.net/demo/Drop-Down-Combo-Tree/")
driver.maximize_window()
driver.find_element(By.ID,'justAnInputBox').click()
time.sleep(2)

def multi_select_dropdown(dropdown_element_list, select_values):
    if select_values[0] == 'all':
        try:
            for ele in dropdown_element_list:
                if ec.element_to_be_clickable(ele):
                    ele.click()
        except Exception as e:
            print(e)

    else:
        for e in dropdown_element_list:
            for v in select_values:    # select_values are list of text/string values to be passed
                if e.text == v:
                    e.click()
                    break # break inner for loop

'''
def multi_select_dropdown(dropdown_element_list,select_values):

    if not select_values[0] == 'all':
        for e in dropdown_element_list:
            for v in range(len(select_values)):
                if e.text == select_values[v]:
                    e.click()
                    break
    else:
        try:
            for e in dropdown_element_list:
                if ec.element_to_be_clickable(e):
                    e.click()
        except Exception as e:
            print(e)
'''
selection_list = driver.find_elements(By.CSS_SELECTOR,'span.comboTreeItemTitle')
print(len(selection_list))

l=['all']
#l=['choice 2','choice 2 1','choice 2 2','choice 2 3','choice 3','choice 6 2 3','choice 7']
multi_select_dropdown(selection_list,l)
#multi_select_dropdown(selection_list,"choice 3")
#multi_select_dropdown(selection_list,"choice 6 2 3")
'''
for l in selection_list:
    print(l.text)
    if l.text == "choice 2":
        l.click()
'''
time.sleep(2)
driver.close()