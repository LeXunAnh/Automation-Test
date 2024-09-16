from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import csv

driver = webdriver.Chrome()
driver.get('http://sis.ou.edu.vn/')
driver.implicitly_wait(5)

driver.find_element(By.CSS_SELECTOR,'button.login100-form-btn').click()
driver.implicitly_wait(5)

usertype = Select(driver.find_element(By.ID,'form-usertype'))
usertype.select_by_index(0)

with open('test.csv','r',newline='') as f:
    reader = csv.DictReader(f)
    for row in reader:
        user = row['user']
        password = row['password']

(driver.find_element(By.NAME,'form-username')).send_keys(user)
(driver.find_element(By.NAME,'form-password')).send_keys(password)

driver.find_element(By.CLASS_NAME,'m-loginbox-submit-btn').click()
driver.implicitly_wait(5)

driver.find_element(By.CSS_SELECTOR,'svg.feather.feather-user.feather-icon').click()
driver.find_element(By.CSS_SELECTOR,'svg.feather.feather-user.feather-icon').click()
driver.implicitly_wait(5)

info = driver.find_elements(By.CSS_SELECTOR,'li.list-group-item')

for item in  info:
    print(item.find_element(By.CSS_SELECTOR,'b').text)

driver.close()
