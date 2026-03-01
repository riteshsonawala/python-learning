stock_sympbols: list[str] = ["MSFT", "GOOG", "AAPL", "NVDA", "AMZN"]

dict_stock_symbols: dict[str, str] = {"MSFT": "Microsoft", "GOOG": "Alphabet", "AAPL": "Apple", "NVDA": "Nvidia", "AMZN": "Amazon"}

for stock_symbol in stock_sympbols:
    print(stock_symbol)

for stock_symbol, company_name in dict_stock_symbols.items():
    print(f"Stocks for {company_name} with symbol {stock_symbol}")

print(len(stock_sympbols))
print(len(dict_stock_symbols))

print(dict_stock_symbols.get("GOOG"))
print(dict_stock_symbols.get("AAPL"))

if __name__ == "__main__": pass