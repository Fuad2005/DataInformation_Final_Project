from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
import os
import pandas as pd


data_frame = pd.DataFrame(columns=['city', 'brand', 'model', 'year', 'type', 'color', 'engine', 'driven_km', 'transmission', 'drive_unit', 'new', 'price', 'date_of_publication'])

options = Options()
options.add_argument('--ignore-ssl-errors=yes')
options.add_argument('--ignore-certificate-errors')

driver = webdriver.Chrome(service=Service(r'C:\Users\Admin\Desktop\IT\chromedriver-win64\chromedriver.exe'), options=options)
driver.get('https://turbo.az')

wait = WebDriverWait(driver, 10)

original_window = driver.current_window_handle

while True:
    elements = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'products-i__link')))
    
    for i in range(len(elements)):
        elements = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'products-i__link')))
        element = elements[i]
        
        element.click()

        driver.switch_to.window(driver.window_handles[-1])
        # wait = WebDriverWait(driver, 5)
        # info = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'product-properties__i-value')))
        # print(info)
        data = {}
        time.sleep(3)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        info = soup.find_all(class_='product-properties__i-value')
        info_texts = []
        for tag in info:
            try:
                info_texts.append(tag.text)
            except AttributeError:
                info_texts.append('N/A')
        # print(info_texts)

        keys = ['city', 'brand', 'model', 'year', 'type', 'color', 'engine', 'driven_km', 'transmission', 'drive_unit', 'new']
        for index, key in enumerate(keys):
            try:
                data[key] = info_texts[index]
            except (IndexError, AttributeError):
                data[key] = None


        try:
            data['price'] = soup.find(class_='tz-mt-10').text[2:]
        except (AttributeError):
            data['price'] = soup.find(class_='product-price__i--bold').text

        try:
            data['date_of_publication'] = soup.find(class_='product-statistics__i-text').text[0][11:]
        except (IndexError, AttributeError):
            data['date_of_publication'] = None

        data['url'] = driver.current_url

        data_df = pd.DataFrame([data])
        if not data_frame.isin(data_df).all(1).any():
            data_frame = pd.concat([data_frame, data_df], ignore_index=True)

        print(i)
        for window_handle in driver.window_handles:
            if window_handle != original_window:
                driver.switch_to.window(window_handle)
                driver.close()

        driver.switch_to.window(original_window)
        
        if i % 10 == 0:
            if os.path.isfile('data.csv'):
                data_frame.to_csv('data.csv', mode='a', index=False, header=False)
            else:
                data_frame.to_csv('data.csv', index=False)
            data_frame = pd.DataFrame()
            driver.execute_script("window.scrollBy(0, 1000);")



