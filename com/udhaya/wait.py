import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


name="Udhaya"


serv=Service("/Users/kumaran/Downloads/chromedriver_win32/chromedriver.exe")
driver=webdriver.Chrome(service=serv)

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()

driver.implicitly_wait(4)

# maximum it waits 6s in the page 
driver.find_element(By.CLASS_NAME,"search-keyword").send_keys("on")
time.sleep(3)
#veg=driver.find_elements(By.CLASS_NAME,"product-name")
veg=driver.find_elements(By.XPATH,"//div[@class='products']/div")
count=len(veg)
print(count)
assert len(veg) > 0

for vegs in veg:
    print(vegs.text)
    vegs.find_element(By.XPATH,"h4").text
    vegs.find_element(By.XPATH,"div/button").click()
    
driver.find_element(By.XPATH,"//img[@alt='Cart']").click()
driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()

#Sum validation

price=driver.find_elements(By.XPATH,"//tr/td[5]/p")
#tr td:nth-child(5) p -->css
sum = 0
for prices in price:
    sum= sum + int(prices.text)
    print(prices.text)
print(sum)

totalAmount=driver.find_element(By.CLASS_NAME,"totAmt").text

assert sum == int(totalAmount)

discountAmount=int(driver.find_element(By.CLASS_NAME,"discountAmt").text)
assert sum == discountAmount
#time.sleep(8)
driver.find_element(By.XPATH,"//input[@class='promoCode']").send_keys("rahulshettyacademy")
driver.find_element(By.XPATH,"//button[@class='promoBtn']").click()


#time.sleep(8)

#Explicitly wait
wait=WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME,"promoInfo")))

print(driver.find_element(By.CLASS_NAME,"promoInfo").text)




#driver.find_element(By.XPATH,"//button[text()='Place Order']").click()
time.sleep(8)

