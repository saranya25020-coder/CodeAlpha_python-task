prices = {
    "AAPL": 180,
    "TSLA": 250,
    "MSFT": 420,
    "NVDA": 135
}

portfolio = {}
total = 0

print("Mini Stock Portfolio Tracker")
print("Available stocks:", ", ".join(prices))

while True:
    stock = input("\nStock name (or 'done'): ").strip().upper()

    if stock == "DONE":
        break

    if stock not in prices:
        print("Stock not found. Choose from the list.")
        continue

    try:
        quantity = int(input(f"How many {stock} shares? "))
        if quantity <= 0:
            print("Enter a quantity greater than zero.")
            continue
    except ValueError:
        print("Please enter a whole number.")
        continue

    portfolio[stock] = portfolio.get(stock, 0) + quantity

print("\nYour portfolio:")
for stock, quantity in portfolio.items():
    value = prices[stock] * quantity
    total += value
    print(f"{stock}: {quantity} shares = ${value:,.2f}")

print(f"Total investment: ${total:,.2f}")