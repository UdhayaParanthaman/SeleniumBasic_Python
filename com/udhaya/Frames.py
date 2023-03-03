import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


serv=Service("/Users/kumaran/Downloads/chromedriver_win32/chromedriver.exe")
driver=webdriver.Chrome(service=serv)

driver.get("https://the-internet.herokuapp.com/iframe")
driver.maximize_window()
driver.implicitly_wait(5)
driver.switch_to.frame("mce_0_ifr")

driver.find_element(By.ID,"tinymce").clear()
driver.find_element(By.ID,"tinymce").send_keys("My name is Udhaya")

driver.switch_to.default_content()
print(driver.find_element(By.CSS_SELECTOR,"h3").text)

time.sleep(8)