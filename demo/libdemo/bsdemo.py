
with open("sample.html") as f:
    contents = f.read()

from bs4 import BeautifulSoup

soup = BeautifulSoup(contents, 'html.parser')
print(soup.h1.text.strip())

links = soup.find_all("a")
for link in links:
    print(link.text.strip())
    print(link.attrs.get('href').strip())


p = soup.find('p', class_ = "intro")
print(p.text.strip())
