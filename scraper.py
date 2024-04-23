from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


data = {
    'city': 'str',
    'brand': 'str',
    'model': 'str',
    'type': 'str',
    'color': 'str',
    'engine': 'str',
    'driven_km': 'str',
    'gearbox': 'str',
    'new': 'bool',
    'condition': 'str',
    'drivetrain': 'str',
    'price': 'int',
    'year': 'int'
}



driver = webdriver.Chrome(service=Service(r'C:\Users\Admin\Desktop\IT\chromedriver-win64\chromedriver.exe'))
driver.get('https://turbo.az')

body = driver.find_element(By.TAG_NAME,'body')
body.click()

while True:
    time.sleep(1)
    body.send_keys(Keys.PAGE_DOWN)
    time.sleep(1)
