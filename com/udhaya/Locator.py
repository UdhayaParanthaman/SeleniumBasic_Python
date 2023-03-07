import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

chrome_Option=webdriver.ChromeOptions() # All the behaviour given to the chrome By Using ChromeOptions
chrome_Option.add_argument("--start-maximized")
chrome_Option.add_argument("--ignore-certificate-errors")

serv=Service("/Users/kumaran/Downloads/chromedriver_win32/chromedriver.exe")

driver=webdriver.Chrome(service=serv,options=chrome_Option)

driver.get("https://rahulshettyacademy.com/angularpractice/")

print(driver.title)
time.sleep(8)