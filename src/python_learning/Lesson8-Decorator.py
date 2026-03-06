import time
from functools import wraps
from typing import Callable


class Trade:
    def __init__(self, symbol: str, price: float, quantity: int):
        self.symbol = symbol
        self.price = price
        self.quantity = quantity



def timed(func : Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Function {func.__name__} executed in {execution_time} seconds")
        return result
    return wrapper

@timed
def create_trade(symbol, price, quantity) -> Trade:
    return Trade(symbol, price, quantity)

def calculate_trade_value(trade):
    return trade.price * trade.quantity

if __name__ == "__main__":
    trade = create_trade("AAPL", 150.0, 10)
    print(f"Trade details: {trade.symbol}, {trade.price}, {trade.quantity}")
    print(f"Trade value: {calculate_trade_value(trade)}")

