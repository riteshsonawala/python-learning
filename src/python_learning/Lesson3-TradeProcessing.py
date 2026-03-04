# You have a list of trades (each trade is a dict)
# 1. Find all unique symbols traded (use a set)
# 2. Find the total value of all trades (quantity * price)
# 3. Find the most expensive trade
# 4. Group trades by symbol into a dict {symbol: [trades]}

trades = [
    {"symbol": "AAPL", "quantity": 100, "price": 185.50},
    {"symbol": "GOOGL", "quantity": 50,  "price": 140.00},
    {"symbol": "AAPL", "quantity": 200, "price": 186.00},
    {"symbol": "MSFT", "quantity": 75,  "price": 375.00},
    {"symbol": "GOOGL", "quantity": 30,  "price": 141.00},
]


total_value : float = 0.0
most_expensive_trade = {"symbol": "", "quantity": 0, "price": 0.0}
grouped_trades : dict[str, list] = {}

unique_symbols = {trade["symbol"] for trade in trades}
total_value = sum([trade["quantity"] * trade["price"] for trade in trades])
for trade in trades:
    # total_value += trade["quantity"] * trade["price"]
    if trade["quantity"] * trade["price"] > most_expensive_trade["price"] * most_expensive_trade["quantity"]:
        most_expensive_trade = trade

    grouped_trades.setdefault(trade["symbol"], []).append(trade)


print(unique_symbols)
print(total_value)
print(most_expensive_trade)

for symbol, trades in grouped_trades.items():
    print(symbol)
    for trade in trades:
        print(trade)
    print("---")

if __name__ == "__main__": pass