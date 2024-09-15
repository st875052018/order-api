class Address:
    def __init__(self, city, district, street):
        self.city = city
        self.district = district
        self.street = street

    def to_dict(self):
        return {
            'city': self.city,
            'district': self.district,
            'street': self.street
        }
