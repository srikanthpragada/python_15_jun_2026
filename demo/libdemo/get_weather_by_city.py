import requests

city = input("Enter city name: ")
response = requests.get(f"https://geocoding-api.open-meteo.com/v1/search?name={city}")

if response.status_code != 200:
    print(f'Sorry! Could not get a weather report for {city}')
    exit()

details = response.json()
lat = details["results"][0]["latitude"]
long = details["results"][0]["longitude"]

print(f"Getting weather for {lat} and {long} ...")

response = requests.get(f'https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={long}&current=temperature_2m')

if response.status_code != 200:
    print('Sorry! Could not get a weather forecast')
    exit()

data = response.json()  # Convert JSON to dict
print('Temperature = ', data['current']['temperature_2m'])


