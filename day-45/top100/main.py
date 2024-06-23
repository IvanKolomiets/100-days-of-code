import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇


response = requests.get(URL)
soap = BeautifulSoup(response.text, 'html.parser')

result_list = [ item.text for item in soap.find_all('h3', class_='title')]

with open('movies.txt',"w") as result:
  for line in reversed(result_list):
    result.write(f"{line}\n")