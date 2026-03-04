class Trade:
            exchange: str = "NYSE"

            def __init__(self, stock, price, quantity):
                self.stock = stock
                self._price = price
                self.quantity = quantity

            def get_trade_value(self):
                return self._price * self.quantity

            @property
            def price(self):
                return self._price

            @price.setter
            def price(self, value) -> None:
                self._price = value

if __name__ == "__main__":
    trade = Trade("AAPL", 150.0, 10)
    print(f"Trade details: {trade.stock}, {trade._price}, {trade.quantity}")
    print(f"Trade value: {trade.get_trade_value()}")
    print(f"Exchange: {trade.exchange}")

