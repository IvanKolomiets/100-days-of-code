import requests
from bs4 import BeautifulSoup
import smtplib, os

URL = 'https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6'
BUY_PRICE = 77
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD")
SMTP_ADDRESS = os.getenv("SMTP_ADDRESS")
SMTP_USER = os.getenv("SMTP_USER")

response = requests.get(f"{URL}", 
                        headers={"Content-Type":"text/html",
                                 "User-Agen":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"}, 
                        verify=False)

soup = BeautifulSoup(response.text,'html.parser')
try:
    price = float(soup.find(class_='a-offscreen').text[1:])
    print(price)
except:
    print(soup.find_all(class_='a-offscreen'))
    exit()

if price < BUY_PRICE:
    with smtplib.SMTP(SMTP_ADDRESS, port=587) as connection:
        connection.starttls()
        result = connection.login(SMTP_USER, SMTP_PASSWORD)
        connection.sendmail(
            from_addr=SMTP_USER,
            to_addrs=SMTP_USER,
            msg=f"Subject:Amazon Price Alert!\n\nCurrent price is {price}, go fast through link {URL}".encode("utf-8")
        )

