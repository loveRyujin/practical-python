# pcost.py
#
# Exercise 1.27

with open('Data/portfolio.csv', 'r') as f:
    _ = next(f)
    count = 0
    for line in f:
        _, stock, price = line.split(',')
        stock = int(stock.strip())
        price = float(price.strip())
        count += stock * price
    print(f'Total cost {count:0.2f}')
        