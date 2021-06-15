import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait



driver = webdriver.Chrome(executable_path="/Users/ilangovanponnuraman/Downloads/chromedriver-2")
driver.get('https://qa-member.astm.org/MyASTM')
wait = WebDriverWait(driver, 6)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "input[name='userName']")))
driver.find_element_by_name("userName").send_keys("dcaullwine@yopmail.com")
driver.find_element_by_name("password").send_keys("Astm1234#")

driver.find_element_by_xpath("//button[@type='submit']").click()

if driver.title == 'ASTM Login':
    print('invalid credentials')
elif driver.title == 'ASTM International - Membership':
    print('login successful')
    time.sleep(10)
    driver.find_element_by_id("dropdown-menu-align-right").click()
    driver.find_element_by_css_selector("button[class ='dropdown-item']").click()