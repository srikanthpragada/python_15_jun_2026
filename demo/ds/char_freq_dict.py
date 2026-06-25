st = "how do you do"

freq = {}
for c in sorted(set(st)):
    freq[c] = st.count(c)

print(freq)


