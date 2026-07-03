# Check whether the number taken on command-line is prime

import sys

if len(sys.argv) < 2:
    print("Number is missing!")
    exit(1)


num = int(sys.argv[1])

for i in range(2, num // 2 + 1):
    if num % i == 0:
        print('Not a prime number')
        break
else:
    print('Prime number')
