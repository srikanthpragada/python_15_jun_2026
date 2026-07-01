def longname(st: str) -> bool:
    return len(st) > 4


names = ['python', 'Java', 'SQL', 'javascript', 'C#']

for name in filter(longname, names):
    print(name)

for name in filter(lambda st: len(st) > 4, names):
    print(name)