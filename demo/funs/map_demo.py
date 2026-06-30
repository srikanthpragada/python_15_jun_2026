
def first_3(st : str) -> str:
    return st[:3]

names = ['python', 'Java', 'SQL', 'javascript', 'C#']

for name in map(first_3, names):
    print(name)


