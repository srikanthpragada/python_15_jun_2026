
names = ['andy', 'Bob', 'Kevin', 'james', 'Peter']

for name in sorted(names):
    print(name, end =  ' ')

print("\n\n")
for name in sorted(names, key = str.lower):
    print(name, end =  ' ')