import json

with open("products.json", "r") as f:
    products = json.load(f)

start = int(input("Enter start price :"))
end = int(input("Enter end price :"))

for product in products:
    price = product["price"]
    if price >= start and price <= end:
        print(f"{product['name']:20}  {product['price']:6.0f}  {product['qty']:2}")







