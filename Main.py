from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://vnexpress.net/')

print(driver.title)
articles = driver.find_elements(By.CSS_SELECTOR,'article.item-news')

for item in articles:
    try:
        print(item.find_element(By.TAG_NAME,'h3').text)
        print(item.find_element(By.TAG_NAME,'p').text)
        print(item.find_element(By.CSS_SELECTOR,'h3.title-news>a').get_attribute('href'))
        print("-------------------------------------")
    except NoSuchElementException:
         print("Not Found")

driver.close()
#-----------------------------------------------------------------------

# # Import the required modules
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# # Create a webdriver instance
# driver = webdriver.Chrome()
#
# # Navigate to the web page
# driver.get("https://vnexpress.net/")
#
# # Wait for the page to load
# wait = WebDriverWait(driver, 10)
#
# # Find all the elements that contain the news titles
# title_elements = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//h3[@class='title-news']/a")))
#
# # Loop through each element and get the text of the title
# for title_element in title_elements:
#     title = title_element.get_attribute("textContent")
#     link = title_element.get_attribute("href")
#     # Print the title
#     print(title)
#     print(link)
#
# # Close the driver
# driver.quit()
#----------------------------------------------------------------------------

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Create a webdriver instance
driver = webdriver.Chrome()

# Navigate to the web page
driver.get("https://vnexpress.net/")

# Wait for 5 seconds to let the page load
#time.sleep(5)

# Find all the elements that contain the news titles
title_elements = driver.find_elements(By.XPATH, "//h3[@class='title-news']/a")

# Loop through each element and get the text of the title and the link
for title_element in title_elements:
    title = title_element.get_attribute("textContent")
    link = title_element.get_attribute("href")
    # Print the title and the link
    print(title, link)

# Close the driver
driver.quit()