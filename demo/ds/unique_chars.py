# Take 5 names and display all unique chars
uchars = set()

for i in range(5):
    name = input("Enter a name :")
    uchars = uchars | set(name)

print("".join(uchars))



