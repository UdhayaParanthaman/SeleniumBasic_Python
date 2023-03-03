import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


serv=Service("/Users/kumaran/Downloads/chromedriver_win32/chromedriver.exe")
driver=webdriver.Chrome(service=serv)

driver.get("https://rahulshettyacademy.com/loginpagePractise/")
driver.maximize_window()
driver.implicitly_wait(7)

driver.find_element(By.CLASS_NAME,"blinkingText").click()

windowOpen=driver.window_handles
driver.switch_to.window(windowOpen[1])

userName=driver.find_element(By.XPATH,"//a[text()='mentor@rahulshettyacademy.com']").text
print(userName)
driver.switch_to.window(windowOpen[0])
driver.find_element(By.ID,"username").send_keys(userName)
driver.find_element(By.ID,"password").send_keys(userName)
driver.find_element(By.ID,"signInBtn").click()

#Explicit Wait
wait=WebDriverWait(driver,10)
wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".alert-danger")))
print(driver.find_element(By.CLASS_NAME,"alert-danger").text)
time.sleep(8)