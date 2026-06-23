# char freqency
st = "how do you do"

visited = []

for c in st:
    if c not in visited:
        print(c, st.count(c))
        visited.append(c)



