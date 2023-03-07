import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

chrome_Option=webdriver.ChromeOptions()
chrome_Option.add_argument("headless")
chrome_Option.add_argument("--ignore-certificate-errors")

serv=Service("/Users/kumaran/Downloads/chromedriver_win32/chromedriver.exe")
driver=webdriver.Chrome(service=serv,options=chrome_Option)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
driver.implicitly_wait(5)
driver.get_screenshot_as_file("screen.png")
driver.execute_script("window.scrollTo(0,600);")
#document.body.scrollHeight);")

time.sleep(8)