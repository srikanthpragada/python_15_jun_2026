from bs4 import BeautifulSoup
import requests
import re

website = "https://www.w3schools.com"
response = requests.get(website)
soup = BeautifulSoup(response.content, 'html.parser')

print(soup.title.text.strip())

# Display links
links = soup.find_all("a")

ulinks = {}

for link in links:
    text = link.text.strip()
    href = link.attrs.get('href','None').strip()
    if text == '' or href == 'None':
        continue

    if href.startswith("javascript"):
        continue

    if not href.startswith("http"):
        href = website + href


    if text[0].isalpha():
        text = re.sub(r'\s+', ' ', text)
        ulinks[str(href)] = text

for href, text in ulinks.items():
    print(text)
    print(href)
    print('-' * 50)



