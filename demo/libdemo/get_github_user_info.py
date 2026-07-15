import requests
user = input("Enter git user id [default srikanthpragada] :")
if user == "":
    user = "srikanthpragada"

resp = requests.get(f"https://api.github.com/users/{user}")
if resp.status_code != 200:
    print("Sorry! Could not get details")
    exit(1)

details = resp.json() # JSON to dict

print('Name    :', details['name'])
print('Company :', details['company'])
print('Location:', details['location'])