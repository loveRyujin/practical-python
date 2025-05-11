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