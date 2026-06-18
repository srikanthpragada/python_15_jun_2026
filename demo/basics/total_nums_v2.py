total = 0
while True:
    v = int(input("Enter a number [0 to stop] :"))
    if v == 0:
        break
    total += v

print('Total', total)
