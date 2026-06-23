# Remove digits from a string
st = "abc123xyz98"

nst = ''
for c in st:
    if not c.isdigit():
        nst += c

print(nst)