from bs4 import BeautifulSoup
import requests

response = requests.get("https://www.tiobe.com/tiobe-index")
if response.status_code != 200:
    print('Sorry! Could not get the TIOBE index')
    exit()

soup = BeautifulSoup(response.content, 'html.parser')

table = soup.find(id="top20")
rows = table.find_all("tr")

# Take rows other than heading at rows[0]
for row in rows[1:11]:
    cols = row.find_all("td")
    lang = cols[4].text.strip()
    rank = cols[5].text.strip()
    print(f"{lang:20}  {rank}")




