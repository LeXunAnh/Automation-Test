import csv
import time
from selenium import webdriver
from selenium.common import NoSuchElementException, ElementNotInteractableException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#Setup
driver = webdriver.Chrome()
driver.maximize_window()
#query link
driver.get('https://www.thegioididong.com/')
time.sleep(3)
driver.find_element(By.CSS_SELECTOR,'body > header > div.header__main > div > ul > li:nth-child(1)').click()
driver.implicitly_wait(5)

while True:
    try:
        # Wait for the "View More" button to be clickable and then click it
        view_more_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'div.view-more a'))
        )
        view_more_button.click()
        time.sleep(3)  # Adjust sleep time if needed
    except (NoSuchElementException, ElementNotInteractableException, TimeoutException):
        break  # Exit the loop if the button is not found or not interactable

listDTs = driver.find_elements(By.CSS_SELECTOR,'#categoryPage > div.container-productbox > ul > li')
driver.implicitly_wait(30)
count =0

for item in listDTs:
    try:
        # Click on the product
        item.click()
        driver.implicitly_wait(30)

        #Xu ly
        count += 1

        #Quay lai trang list
        driver.execute_script("window.history.go(-1)")
        driver.implicitly_wait(30)

    except NoSuchElementException:
        print("Pass")

print(count)
driver.close()