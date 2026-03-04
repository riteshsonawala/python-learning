trades = [
    {"symbol": "AAPL", "quantity": 100, "price": 185.50},
    {"symbol": "GOOGL", "quantity": 50,  "price": 140.00},
    {"symbol": "AAPL", "quantity": 200, "price": 186.00},
    {"symbol": "MSFT", "quantity": 75,  "price": 375.00},
    {"symbol": "GOOGL", "quantity": 30,  "price": 141.00},
]

# 1. Write a function calculate_value(trade) that returns quantity * price
def calculate_value(trade):
    return trade["quantity"] * trade["price"]

# 2. Write a function filter_trades(trades, min_value) that returns
#    only trades above min_value — use a comprehension inside
def filter_trades(trades: list, min_value: int) -> list:
    return [trade for trade in trades if calculate_value(trade) > min_value]

# 3. Write a function sort_trades(trades, by="price") that sorts trades
#    by "price", "quantity", or "value" depending on the 'by' argument
def sort_trades(trades: list, sort_by: str) -> list:
    return sorted(trades, key=lambda trade: trade[sort_by])

# 4. Write a function summarise(trades, formatter) where formatter is
#    a function that takes a trade and returns a string.
#    Call summarise with two different formatters:
#    - one that prints "AAPL: $18,550.00"
#    - one that prints "AAPL x 100 @ $185.50"
def summarise(trades: list, formatter) -> None:
    for trade in trades:
        print(formatter(trade))

formatter1 = lambda trade: f"{trade['symbol']}: ${calculate_value(trade):.2f}"
formatter2 = lambda trade: f"{trade['symbol']} x {trade['quantity']} @ ${trade['price']:.2f}"

if __name__ == "__main__":
    print(calculate_value(trades[0]))
    print(filter_trades(trades, 1000))
    print(sort_trades(trades, "price"))
    summarise(trades, formatter1)
    summarise(trades, formatter2)

