from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common import NoSuchElementException
from selenium.webdriver.support.ui import Select
import csv

driver = webdriver.Chrome()
driver.get('https://www.google.com/')
driver.implicitly_wait(5)

const = driver.find_element(By.NAME,'q')
const.send_keys("")
const.submit()
driver.implicitly_wait(10)

results = driver.find_elements(By.CSS_SELECTOR, 'div.g')

with open('ListGG.csv', 'w', newline='', encoding='utf-8') as f:
    fieldName = ['Title', 'Link']
    writer = csv.DictWriter(f, fieldnames=['Title', 'Link'])
    writer.writeheader()

    for re in results:
        try:
            # print(re.find_element(By.CSS_SELECTOR,'a').text)
            # print(re.find_element(By.CSS_SELECTOR,'a').get_attribute('href'))
            # print("---------------------------------")
            title = re.find_element(By.CSS_SELECTOR,'a').text
            link = re.find_element(By.CSS_SELECTOR,'a').get_attribute('href')

            writer.writerow({'Title': title, 'Link': link})

        except NoSuchElementException:
            print("Pass")

driver.close()

