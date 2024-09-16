from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common import NoSuchElementException
from selenium.webdriver.support.ui import Select
import csv

driver = webdriver.Chrome()
driver.get('https://www.youtube.com/')
driver.implicitly_wait(5)

query = driver.find_element(By.NAME,'search_query')
query.send_keys("Phuong My Chi")
query.submit()

driver.implicitly_wait(10)
videos = driver.find_elements(By.CSS_SELECTOR,'ytd-video-renderer')

with open('List.csv','w',newline='',encoding='utf-8') as f:
    fieldName = ['Title','Link']
    writer = csv.DictWriter(f, fieldnames=['Title', 'Link'])
    writer.writeheader()

    for item in videos:
        try:
            # print(item.find_element(By.CSS_SELECTOR,'#video-title').text)
            # print(item.find_element(By.CSS_SELECTOR, 'a').get_attribute('href'))
            # print("---------------------------------")
            title = item.find_element(By.CSS_SELECTOR,'#video-title').text
            link = item.find_element(By.CSS_SELECTOR, 'a').get_attribute('href')

            writer.writerow({'Title': title, 'Link': link})

        except NoSuchElementException:
            print("Pass")

driver.close()
