# Check whether the number taken on command-line is prime

import sys

if len(sys.argv) < 2:
    print("Number is missing!")
    exit(1)

for data in sys.argv[1:]:
    if not data.isdigit():
        continue

    num = int(data)

    for i in range(2, num // 2 + 1):
        if num % i == 0:
            print(f'{num} is not a prime number')
            break
    else:
        print(f'{num} is a prime number')
