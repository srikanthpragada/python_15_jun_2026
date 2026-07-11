import re

f = open("customers.txt", "rt")
phones = {}  # Empty dictionary
for line in f.readlines():
    # Split line into two parts – name and phone
    parts = line.strip().split(",")
    # Ignore line if it doesn’t contain 2 parts
    if len(parts) != 2:
        continue

    mobile = parts[1].strip()
    # Check validity of mobile number
    m = re.fullmatch(r'\d{10}',mobile)
    if m is None:  # invalid mobile number
        continue

    # Add entry to dictionary
    phones[parts[0]] = mobile

# sort by names and print along with phone number
for name, phone in sorted(phones.items()):
    print(f"{name:20}  {phone}")
