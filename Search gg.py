# import time
# from selenium import webdriver
# from selenium.common import NoSuchElementException
# from selenium.webdriver.common.by import By
#
# driver = webdriver.Chrome()
# driver.get('https://www.youtube.com/')
#
#
# input= driver.find_element(By.CSS_SELECTOR,'input#search')
# input.send_keys("python")
# input.submit()
#
# # elements = driver.find_elements(By.ID,'#thumbnail')
# # for item in elements:
# # print(item.find_element(By.CSS_SELECTOR,'div#contents a#thumbnail').get_attribute('href'))
#
# hrefs = [video.get_attribute('href') for video in driver.find_elements(By.ID,"thumbnail")]
# for href in hrefs:
#     print(href)
# #time.sleep(5)
# #------------------------------------------------------
import time

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from  selenium.webdriver.common.by import By

# Create a webdriver instance
driver = webdriver.Chrome()

# Navigate to the Google homepage
driver.get("https://www.google.com/")

# Find the search box element
search_box = driver.find_element(By.NAME,"q")

# Enter the query in the search box
query = "kiem thu phan mem"
search_box.send_keys(query)
search_box.submit()

# Press the enter key to submit the query
#search_box.send_keys(Keys.RETURN) = .summit()

time.sleep(5)

elements = driver.find_elements(By.TAG_NAME, "h3")

for item in elements:
    try:
        title = item.text
        link = item.find_element(By.XPATH,"..").get_attribute("href")
        print(title,link)
    except NoSuchElementException:
        print("pass")


# Close the driver
driver.quit()
