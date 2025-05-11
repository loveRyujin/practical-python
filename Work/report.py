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
            stock = int(row[1].strip())
            price = float(row[2].strip())
            portfolio.append((row[0], stock, price))

    return portfolio