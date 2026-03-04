trades = [
    {"symbol": "AAPL", "quantity": 100, "price": 185.50},
    {"symbol": "GOOGL", "quantity": 50,  "price": 140.00},
    {"symbol": "AAPL", "quantity": 200, "price": 186.00},
    {"symbol": "MSFT", "quantity": 75,  "price": 375.00},
    {"symbol": "GOOGL", "quantity": 30,  "price": 141.00},
]

# 1. Create a list of all trade values (quantity * price)
list_of_all_trade_values = [trade["quantity"] * trade["price"] for trade in trades]
print(list_of_all_trade_values)
# 2. Create a list of symbols for trades worth more than $20,000
list_of_symbols_for_trades_worth_more_than_20k = {trade["symbol"] for trade in trades if trade["quantity"] * trade["price"] > 20000}
print(list_of_symbols_for_trades_worth_more_than_20k)
# 3. Create a dict of {symbol: total_quantity}
#    Hint: this one is tricky with just a comprehension — try it,
#    it's ok to use a loop if you get stuck
dict_of_symbol_total_quantity={trade["symbol"]: trade["quantity"] for trade in trades}
print(dict_of_symbol_total_quantity)
# 4. Create a list of strings formatted like "AAPL: 100 @ $185.50"
#    for every trade
dict_of_symbol_and_formated_string = {trade["symbol"]: f"{trade['symbol']}: {trade['quantity']} @ ${trade['price']:.2f}" for trade in trades}
print(dict_of_symbol_and_formated_string)