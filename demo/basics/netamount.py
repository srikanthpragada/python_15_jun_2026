# Take qty and price and display net amount
# 20% if qty is 2 or more otherwise 10%

qty = int(input("Enter quantity :"))
price = int(input("Enter price :"))
amount = qty * price

if qty >= 2:
    discount = amount * 20 // 100
else:
    discount = amount * 10 // 100

net_amount = amount - discount

print(f"Net amount : {net_amount}")

