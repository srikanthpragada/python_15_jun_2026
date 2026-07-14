import requests

response = requests.get("https://official-joke-api.appspot.com/random_joke")

if response.status_code != 200:
    print('Sorry! Could not get a joke!')
    exit()

joke = response.json()  # Convert JSON to dict

print(joke['setup'])
print(joke['punchline'])




