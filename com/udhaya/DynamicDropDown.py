import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


ser=Service("/Users/kumaran/Downloads/chromedriver_win32/chromedriver.exe")
driver=webdriver.Chrome(service=ser)
driver.get("https://www.makemytrip.com/flights/")

driver.maximize_window()
time.sleep(3)
driver.find_element(By.CSS_SELECTOR,"label[for='fromCity']").click()
driver.find_element(By.CLASS_NAME,"react-autosuggest__input.react-autosuggest__input--open").send_keys("che")
time.sleep(3)
variables=driver.find_elements(By.CSS_SELECTOR,"p[class='font14 appendBottom5 blackText']")

print(len(variables)) 

for var in variables:
    print(var.text)
    if var.text=="Chennai, India":
        time.sleep(3)
        var.click()
        print("Condition satisfied")
        break
    else:
        print("not entered ")
print(driver.find_element(By.CLASS_NAME,"react-autosuggest__input.react-autosuggest__input--open").text)
time.sleep(30)



