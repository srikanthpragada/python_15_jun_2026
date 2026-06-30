
def invert(st : str) -> str:
    ns = ""
    for c in st:
        if c.isupper():
            ns += c.lower()
        else:
            ns += c.upper()

    return ns



names = ['python', 'Java', 'SQL', 'javascript', 'C#']

for name in map(invert, names):
    print(name)


