def hasupper(st: str) -> bool:
    for c in st:
        if c.isupper():
            return True

    return False


names = ['python', 'Java', 'SQL', 'javascript', 'C#']

for name in filter(hasupper, names):
    print(name)
