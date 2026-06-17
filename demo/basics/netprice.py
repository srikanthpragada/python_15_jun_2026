# Take price and display net price after a discount of 12%

price = int(input("Enter price :"))
discount = price * 12 // 100
net_price = price - discount
print(f'Net price = {net_price}')
