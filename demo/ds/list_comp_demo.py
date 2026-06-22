st = "Python"

codes = []
for c in st:
    codes.append(ord(c))

print(codes)

# list comprehension
codes = [ord(c) for c in st if c.islower()]
print(codes)

