from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
from selenium.webdriver.common.by import By
from time import sleep
import os

PHONE = os.environ('PHONE')

class TinderSwiper:
    driver: webdriver
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)

    def __del__(self):
        self.driver.quit()
        print('Destructor called, Employee deleted.')

    def accept_cookie(self):
        try:
            cookies_button = self.driver.find_element(By.XPATH, value='//*[text()="I accept"]')
            cookies_button.click()
        except:
            print('Cookie failed')
            sleep(5)
            self.accept_cookie()

    def click_login(self):
        try:
            log_in_button = self.driver.find_element(By.XPATH, value='//*[text()="Log in"]')
            log_in_button.click()
        except:
            print('Log in by phone click button failed')
            sleep(5)
            self.click_login()

    def click_log_in_with_phone_number(self):
        try:
            by_phone_button = self.driver.find_element(By.CSS_SELECTOR, value="button[aria-label='Log in with phone number']")
            by_phone_button.click()
        except:
            print('Log in failed')
            sleep(5)
            self.click_log_in_with_phone_number()

    def text_phone_nubmer_and_submit(self):
        try:
            phone_input = self.driver.find_element(By.CSS_SELECTOR, value="input[name='phone_number']")
            phone_input.send_keys(PHONE)
            next_button = self.driver.find_element(By.XPATH, value='//*[text()="Next"]')
            next_button.click()
        except:
            print('Fail in prompting the phone number')

    def do_login(self):
        self.driver.get("https://tinder.com/")
        sleep(15)
        
        self.accept_cookie()
        sleep(8)

        self.click_login()
        sleep(8)

        self.click_log_in_with_phone_number()
        sleep(8)

        self.text_phone_nubmer_and_submit()

    def do_all_confirmations(self):
        try:
            allow_location_button = self.driver.find_element(By.CSS_SELECTOR, value="button[aria-label='Allow']")
            allow_location_button.click()
            sleep(2)
            miss_out_button = self.driver.find_element(By.CSS_SELECTOR, value="button[aria-label='I’ll give it a miss']")
            miss_out_button.click()
        except:
            print('Fail in prompting the phone number')

    def skip_match(self):
        try:
            match_popup = self.driver.find_element(By.CSS_SELECTOR, value=".itsAMatch a")
            match_popup.click()
        except NoSuchElementException:
            sleep(1)

    def click_like(self):
        try:
            like_button =  self.driver.find_element(By.XPATH, value='//*[@id="t41619109"]/div/div[1]/div/main/div[1]/div/div/div/div[1]/div[1]/div/div[4]/div/div[4]/button')
            like_button.click()
        except ElementClickInterceptedException:
            self.skip_match()
        except:
            print('Something goes wrong')
            try:
                like_button =  self.driver.find_element(By.XPATH, value='//*[@id="t41619109"]/div/div[1]/div/main/div[1]/div/div/div/div[1]/div[1]/div/div[3]/div/div[4]/button')
                print('another one')
                like_button.click()
            except:
                print('another failed, try again')
                self.click_like()

    def do_100_swipes_right(self):
        for n in range(100):
            sleep(5)
            print(f"Do {n+1} swipe")
            self.click_like()


    def do_all_swipes(self):
        self.do_all_confirmations()
        sleep(15)
        self.do_100_swipes_right()


if __name__ == '__main__':
    session = TinderSwiper()
    session.do_login()
    sleep(135)
    session.do_all_swipes()
    del session





