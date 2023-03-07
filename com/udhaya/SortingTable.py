import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

browserSortedVeggies=[]

serv=Service("/Users/kumaran/Downloads/chromedriver_win32/chromedriver.exe")
driver=webdriver.Chrome(service=serv)

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
driver.maximize_window()
driver.implicitly_wait(5)

driver.find_element(By.XPATH,"//span[text()='Veg/fruit name']").click()
vegs=driver.find_elements(By.XPATH,"//tbody/tr/td[1]")
for veg in vegs:
    browserSortedVeggies.append(veg.text)

print(browserSortedVeggies)
originalBrowserSortedList=browserSortedVeggies.copy()

#sort their list 
browserSortedVeggies.sort()

assert browserSortedVeggies == originalBrowserSortedList
print(originalBrowserSortedList)
time.sleep(8)