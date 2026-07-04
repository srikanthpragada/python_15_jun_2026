import pyasn1_modules


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f'{self.name.upper()} - {self.price}'

    def __eq__(self, other):
        return self.name == other.name and self.price == other.price

    def __gt__(self, other):
        return self.price > other.price


p1 = Product("iPhone 16 Pro", 65000)
p2 = Product("iPhone 16 Pro", 65000)
p3 = Product("iPad Air", 55000)

print(p1)
print(p1.__str__())
print(p1 == p2)  # p1.__eq__(p2)
print(p1 > p3)  # p1.__gt__(p2)
print(p2 < p3)
