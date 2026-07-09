import json

with open("products.json", "r") as f:
    products = json.load(f)

total = 0
for product in products:
    print(f"{product['name']:20}  {product['price']:6.0f}")
    total += product['price'] * product['qty']

print(f"Total : {total}:6")





