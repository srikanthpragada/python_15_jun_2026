from datetime import datetime

f = open("players.txt","r")

players = {}
for line in f:
    parts = line.strip().split(",")
    if len(parts) < 2:
        continue

    name = parts[0].strip()
    try:
        dob = datetime.strptime(parts[1], "%d-%m-%Y")
        age = (datetime.now() - dob).days // 365
        players[name] = age
    except ValueError:
        continue


for name, age in sorted(players.items(),
                        key=lambda t: t[1], reverse=True):
    print(f"{name:20}: {age:2}")



