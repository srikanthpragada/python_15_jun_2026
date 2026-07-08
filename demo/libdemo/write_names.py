
names = ['Python', 'Java', 'Javascript', 'C#', 'SQL']
f = open("names.txt", "wt")

for name in names:
    f.write(name + "\n")

f.close()


