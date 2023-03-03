import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


serv=Service("/Users/kumaran/Downloads/chromedriver_win32/chromedriver.exe")
driver=webdriver.Chrome(service=serv)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

# This is one way to select Radio Button
driver.find_element(By.XPATH,"//input[@value='radio1']").click()
driver.find_element(By.XPATH,"//input[@value='radio2']").click()

# This is another way to select Radio Button
radio=driver.find_elements(By.CLASS_NAME,"radioButton")
print(len(radio))
radio[2].click()
assert radio[2].is_selected()


# Is_displayed
assert driver.find_element(By.ID,"displayed-text").is_displayed()
driver.find_element(By.ID,"hide-textbox").click()

assert not driver.find_element(By.ID,"displayed-text").is_displayed()
time.sleep(8)