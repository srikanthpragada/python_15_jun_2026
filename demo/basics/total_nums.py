total = 0
for n in range(1, 11):
    v = int(input("Enter a number [0 to stop] :"))
    if v == 0:
        break
    total += v

print('Total', total)
