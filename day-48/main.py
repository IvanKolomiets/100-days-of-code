from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

# print('Amoazon part')
# driver.get("https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1")
# price_dollars = driver.find_element(By.CLASS_NAME, value="a-price-whole")
# price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction")
# print(f"${price_dollars.text}.{price_cents.text}")

#
###
#

print("locator part")
driver.get("https://www.python.org/")
li_elements = driver.find_elements(By.XPATH, value='//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li')

result = {}
i = 0
for li_element in li_elements:
  time, name = li_element.text.splitlines()
  result[i] = {'time': time, 'name': name}
  i += 1

print(result)

driver.quit()
