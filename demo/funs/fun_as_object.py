def add(a,b):
    return a+b

a = 10
b = a

print(id(a), id(b))

print(add(10,20))
sum = add
print(sum(10,20))

print(id(add), id(sum))


