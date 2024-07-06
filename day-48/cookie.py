from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def by_something(money,store,timeout):
    print('Check balance')
    current_balance = int(money.text.replace(',', ''))
    max_price = 999999999
    for item in reversed(store[1:]):
      if len(item.text) > 2:

        item_price = int(item.text.rsplit(' ',1)[1].replace(',', ''))
        if item_price * 2 > max_price:
           print('too expensive...')
           max_price = item_price
           continue           
        
        if current_balance > item_price:
            print(f"money - {current_balance}, price is {item_price}")
            item.click()
            timeout -= 1
            return
        max_price = item_price
    timeout += 1


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")



cookie = driver.find_element(By.CSS_SELECTOR, value='#cookie')


timeout = 4
first_time = time.time()
last_time = first_time

while(True):
    cookie.click()
    new_time = time.time()
    if  new_time - last_time > timeout:
        money = driver.find_element(By.CSS_SELECTOR, value='#money')
        store = driver.find_elements(By.CSS_SELECTOR, value='#store b')
        by_something(money,store,timeout)
        last_time = new_time