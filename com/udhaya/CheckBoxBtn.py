import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


serv=Service("/Users/kumaran/Downloads/chromedriver_win32/chromedriver.exe")
driver=webdriver.Chrome(service=serv)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

# this is oneway to select checkbox
#driver.find_element(By.ID,"checkBoxOption1").click()
#driver.find_element(By.ID,"checkBoxOption2").click()

# this is another way to select checkbox

checkBox=driver.find_elements(By.XPATH,"//input[@type='checkbox']")
print(len(checkBox))
for check in checkBox:
    if check.get_attribute("value")=="option3":
        check.click()
        assert check.is_selected()
        break
time.sleep(8)