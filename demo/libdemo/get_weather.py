import requests

lat = 17.6868
long = 83.2185
response = requests.get(f'https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={long}&current=temperature_2m')

if response.status_code != 200:
    print('Sorry! Could not get a weather forecast')
    exit()

data = response.json()  # Convert JSON to dict
print(data['current']['temperature_2m'])


