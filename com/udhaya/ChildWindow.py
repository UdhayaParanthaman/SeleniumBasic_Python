import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


serv=Service("/Users/kumaran/Downloads/chromedriver_win32/chromedriver.exe")
driver=webdriver.Chrome(service=serv)

driver.get("https://the-internet.herokuapp.com/windows")
driver.maximize_window()
driver.implicitly_wait(5)
driver.find_element(By.LINK_TEXT,"Click Here").click()

windowsOpened=driver.window_handles 
# window name it will store
# switch to child window
driver.switch_to.window(windowsOpened[1])
print(driver.find_element(By.CSS_SELECTOR,"h3").text)
driver.close()

#switch back to parent window
driver.switch_to.window(windowsOpened[0])
print(driver.find_element(By.CSS_SELECTOR,"h3").text)

#Validation
parentWindowTxt="Opening a new window"
assert parentWindowTxt == driver.find_element(By.CSS_SELECTOR,"h3").text
time.sleep(8)