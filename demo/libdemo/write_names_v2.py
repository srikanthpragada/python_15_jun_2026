names = ['Python', 'Java', 'Javascript', 'C#', 'SQL']

with open("names.txt", "wt") as f:
    for name in names:
        f.write(name + "\n")


