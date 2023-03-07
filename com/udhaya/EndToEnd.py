import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

serv = Service("/Users/kumaran/Downloads/chromedriver_win32/chromedriver.exe")

driver = webdriver.Chrome(service=serv)

driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
driver.implicitly_wait(6)
driver.find_element(By.XPATH, "//a[normalize-space()='Shop']").click()

product = driver.find_elements(By.XPATH, "//div[@class='card h-100']")

for products in product:
    Exact = products.find_element(By.XPATH, "div/h4/a").text
    print(Exact)
    if Exact == "Nokia Edge":
        products.find_element(By.XPATH, "div/button").click()
        # driver.find_element(By.CLASS_NAME,"btn").click()
        break
driver.find_element(By.XPATH, "//div[@class='collapse navbar-collapse']/ul").click()

driver.find_element(By.CLASS_NAME, "btn-success").click()

# Handling Autosuggestion DropDown
driver.find_element(By.ID, "country").send_keys("Ind")

# Explicitly wait
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
driver.find_element(By.LINK_TEXT, "India").click()
driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()

driver.find_element(By.CLASS_NAME, "btn-lg").click()

success_msg = driver.find_element(By.CLASS_NAME, "alert").text
print(success_msg)

assert "Success! Thank you! " in  success_msg

# print(driver.title)
time.sleep(8)
