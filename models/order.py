from models.address import Address

class Order:
    def __init__(self, id, name, address, price, currency):
        self.id = id
        self.name = name
        self.address = address
        self.price = price
        self.currency = currency
