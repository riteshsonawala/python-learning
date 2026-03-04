# 1. Create a custom TradeValidationError exception with fields:
#    symbol, field_name, reason

# 2. Update your Trade dataclass to validate in __init__:
#    - price must be > 0
#    - quantity must be > 0
#    - symbol must not be empty string
#    Raise TradeValidationError for each violation

# 3. Try creating invalid trades and catch the exceptions
#    Print the symbol, field_name and reason from each exception
class TradeValidationError(Exception):
        def __init__(self, symbol, field_name, reason):
            self.symbol = symbol
            self.field_name = field_name
            self.reason = reason
            super().__init__(f"Trade validation error: {symbol} - {field_name}: {reason}")

        def __str__(self):
            return f"Trade validation error: {self.symbol} - {self.field_name}: {self.reason}"

class Trade:
    def __init__(self, symbol, price, quantity):
        self.symbol = symbol
        self.price = price
        self.quantity = quantity

def create_trade(symbol, price, quantity):
    if price <= 0:
        raise TradeValidationError(symbol, "price", "must be > 0")
    if quantity <= 0:
        raise TradeValidationError(symbol, "quantity", "must be > 0")
    if symbol == "":
        raise TradeValidationError(symbol, "symbol", "must not be empty string")
    return Trade(symbol, price, quantity)



if __name__ == "__main__":
    try:
        create_trade("AAPL", 0, 10)
    except TradeValidationError as e:
        print(e)
    try:
        create_trade("GOOG", 10.0, -10)
    except TradeValidationError as e:
        print(e)
    try:
        create_trade("", 10.0, 10)
    except TradeValidationError as e:
        print(e)
