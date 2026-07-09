f = open("customers.txt", "rt")
phones = {}  # Empty dictionary
for line in f.readlines():
    # Split line into two parts – name and phone
    parts = line.strip().split(",")
    # Ignore line if it doesn’t contain 2 parts
    if len(parts) != 2:
        continue
    # Add entry to dictionary
    phones[parts[0]] = parts[1]

# sort by names and print along with phone number
for name, phone in sorted(phones.items()):
    print(f"{name:20}  {phone}")
