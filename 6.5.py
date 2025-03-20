import time

from selenium import webdriver
from pprint import pprint
from selenium.webdriver.common import alert
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By


with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/5.7/1/index.html')
    time.sleep(2)
    for btn in browser.find_elements(By.CLASS_NAME, 'button-container'):
        browser.execute_script("return arguments[0].scrollIntoView(true);", btn)
        time.sleep(1)
        btn.click()
    time.sleep(2)
    alert_text = browser.switch_to.alert.text
    print(alert_text)