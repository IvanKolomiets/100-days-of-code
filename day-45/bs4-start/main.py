from bs4 import BeautifulSoup
# contents=""
with open('website.html') as file:
    contents = file.read()
    # for line in file:
    #     contents +=line
print(contents)

soup = BeautifulSoup(contents, 'html.parser')
print(soup.title)
print(soup.title.name)
print(soup.title.string)
print(soup.prettify())

all_anchor_tags = soup.find_all(name='a')
for tag in all_anchor_tags:
    print(tag.get('href')) 