def uncommon(s1, s2):
    for c in sorted(set(s1) ^ set(s2)):
        print(c, end = '')



uncommon('java', 'oracle')
