import re

class OrderValidator:
    def __init__(self, order):
        self.order = order
        self.errors = []

    def validate(self):
        self.validate_required_fields()
        self.validate_name()
        self.validate_price()
        self.validate_currency()
        self.validate_address()
        return self.errors

    def validate_required_fields(self):
        if not self.order.id:
            self.errors.append("Missing required field: id")
        if not self.order.name:
            self.errors.append("Missing required field: name")
        if not self.order.address:
            self.errors.append("Missing required field: address")
        if not self.order.price:
            self.errors.append("Missing required field: price")
        if not self.order.currency:
            self.errors.append("Missing required field: currency")

    def validate_name(self):
        name = self.order.name or ''
        if not re.match("^[A-Za-z ]+$", name):
            self.errors.append("Name contains non-English characters")
            return

        words = name.split()
        for word in words:
            if not word[0].isupper():
                self.errors.append("Name is not capitalized")
                break

    def validate_price(self):
        try:
            price = float(self.order.price)
            if price > 2000:
                self.errors.append("Price is over 2000")
        except ValueError:
            self.errors.append("Price must be a number")

    def validate_currency(self):
        currency = self.order.currency or ''
        if currency not in ['TWD', 'USD']:
            self.errors.append("Currency format is wrong")

    def validate_address(self):
        address = self.order.address
        if not address.city:
            self.errors.append("Missing required field in address: city")
        if not address.district:
            self.errors.append("Missing required field in address: district")
        if not address.street:
            self.errors.append("Missing required field in address: street")
