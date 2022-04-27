prices = (29.95, 9.9, 4.95, 79.98, 2.97, 4.95)
print(len(prices))
print(prices.count(4.95))
print(prices.index(79.98))
print(79.97 in prices)

for price in prices:
    print(f'{price:.2f}')
