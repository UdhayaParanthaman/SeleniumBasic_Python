import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
name="Udhaya"

serv=Service("/Users/kumaran/Downloads/chromedriver_win32/chromedriver.exe")
driver=webdriver.Chrome(service=serv)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

driver.find_element(By.ID,"name").send_keys(name)
driver.find_element(By.ID,"alertbtn").click()

alert=driver.switch_to.alert # switch to alert window [From driver to alert window]

print(alert.text)

assert name in alert.text
time.sleep(8)
alert.accept()
print("Hello World")
time.sleep(8)