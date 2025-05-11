# report.py
#
# Exercise 2.4
import csv

def read_portfolio(filename):
    with open(filename, "r") as f:
        _ = next(f)  # Skip the header
        rows = csv.reader(f)
        portfolio = []
        for row in rows:
            name = row[0].strip()
            stock = int(row[1].strip())
            price = float(row[2].strip())
            portfolio.append({'name': name, 'shares': stock, 'price': price})

    return portfolio

def read_prices(filename):
    with open(filename, "r") as f:
        rows = csv.reader(f)
        prices = {}
        for row in rows:
            if not row:
                continue
            name = row[0].strip()
            price = float(row[1].strip())
            prices[name] = price

    return prices

portfolio = read_portfolio('Data/portfolio.csv')
prices = read_prices('Data/prices.csv')

# Calculate the total cost of the portfolio
total_cost = 0.0
for s in portfolio:
    total_cost += s['shares']*s['price']

print('Total cost', total_cost)

# Compute the current value of the portfolio
total_value = 0.0
for s in portfolio:
    total_value += s['shares']*prices[s['name']]

print('Current value', total_value)
print('Gain', total_value - total_cost)