from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://en.wikipedia.org/wiki/Main_Page")
# article_count = driver.find_element(By.CSS_SELECTOR, value='#articlecount').text.split()[0]
# print(article_count)
article_count = driver.find_element(By.CSS_SELECTOR, value='#articlecount a')
article_count.click()


driver.get("http://secure-retreat-92358.herokuapp.com/")
fname = driver.find_element(By.NAME, value='fName')
lname = driver.find_element(By.NAME, value='lName')
email = driver.find_element(By.NAME, value='email')
button = driver.find_element(By.CSS_SELECTOR, value='button')

fname.send_keys('Ivan')
lname.send_keys('Petrov')
email.send_keys('sidorov@ya.ru')
button.click()

driver.quit()