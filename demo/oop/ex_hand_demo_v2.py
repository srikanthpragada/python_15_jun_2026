st = input("Enter a number :")
try:
    n = int(st)
    print(100 // n)
except ValueError:
    print("Invalid input")
else:
    print("Success")
finally:
    print("The End!")

print("Done!")






