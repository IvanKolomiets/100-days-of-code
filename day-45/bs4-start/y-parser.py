from bs4 import BeautifulSoup
import requests

uri = 'https://news.ycombinator.com/news'
resp = requests.get(uri)
soup = BeautifulSoup(resp.text, 'html.parser')
spans = soup.find_all(class_='titleline')
for span in spans:
    print(span.a.text)