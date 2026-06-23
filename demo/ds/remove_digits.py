# Remove digits from a string
st = "abc123xyz98"

non_digits = [c for c in st if not c.isdigit()]
nst = "".join(non_digits)

print(nst)




