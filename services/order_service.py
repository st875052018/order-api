class OrderService:
    EXCHANGE_RATE = 31

    def __init__(self, order):
        self.order = order

    def process_order(self):
        currency = self.order.currency
        price = float(self.order.price)

        if currency == 'USD':
            price_in_twd = price * self.EXCHANGE_RATE
            if price_in_twd.is_integer():
                price_in_twd = int(price_in_twd)
            self.order.price = str(price_in_twd)
            self.order.currency = 'TWD'

        return self.order
