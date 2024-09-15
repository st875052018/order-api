import unittest
from app import app

class OrderAPITestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_valid_order(self):
        data = {
            "id": "A0000001",
            "name": "Melody Holiday Inn",
            "address": {
                "city": "taipei-city",
                "district": "da-an-district",
                "street": "fuxing-south-road"
            },
            "price": "2000",
            "currency": "TWD"
        }
        response = self.app.post('/api/orders', json=data)
        self.assertEqual(response.status_code, 200)

    def test_missing_address_fields(self):
        data = {
            "id": "A0000002",
            "name": "Melody Holiday Inn",
            "address": {
                "city": "taipei-city",
                "district": "",
                "street": "fuxing-south-road"
            },
            "price": "1500",
            "currency": "TWD"
        }
        response = self.app.post('/api/orders', json=data)
        self.assertEqual(response.status_code, 400)
        self.assertIn("Missing required field in address: district", response.get_data(as_text=True))

    def test_name_contains_non_english(self):
        data = {
            "id": "A0000001",
            "name": "美樂蒂 Holiday Inn",
            "address": {
                "city": "taipei-city",
                "district": "da-an-district",
                "street": "fuxing-south-road"
            },
            "price": "2000",
            "currency": "TWD"
        }
        response = self.app.post('/api/orders', json=data)
        self.assertEqual(response.status_code, 400)
        self.assertIn("Name contains non-English characters", response.get_data(as_text=True))

    def test_name_not_capitalized(self):
        data = {
            "id": "A0000001",
            "name": "melody Holiday Inn",
            "address": {
                "city": "taipei-city",
                "district": "da-an-district",
                "street": "fuxing-south-road"
            },
            "price": "2000",
            "currency": "TWD"
        }
        response = self.app.post('/api/orders', json=data)
        self.assertEqual(response.status_code, 400)
        self.assertIn("Name is not capitalized", response.get_data(as_text=True))

    def test_price_over_2000(self):
        data = {
            "id": "A0000001",
            "name": "Melody Holiday Inn",
            "address": {
                "city": "taipei-city",
                "district": "da-an-district",
                "street": "fuxing-south-road"
            },
            "price": "2050",
            "currency": "TWD"
        }
        response = self.app.post('/api/orders', json=data)
        self.assertEqual(response.status_code, 400)
        self.assertIn("Price is over 2000", response.get_data(as_text=True))

    def test_currency_wrong_format(self):
        data = {
            "id": "A0000001",
            "name": "Melody Holiday Inn",
            "address": {
                "city": "taipei-city",
                "district": "da-an-district",
                "street": "fuxing-south-road"
            },
            "price": "2000",
            "currency": "EUR"
        }
        response = self.app.post('/api/orders', json=data)
        self.assertEqual(response.status_code, 400)
        self.assertIn("Currency format is wrong", response.get_data(as_text=True))

    def test_currency_usd_conversion(self):
        data = {
            "id": "A0000001",
            "name": "Melody Holiday Inn",
            "address": {
                "city": "taipei-city",
                "district": "da-an-district",
                "street": "fuxing-south-road"
            },
            "price": "50",
            "currency": "USD"
        }
        response = self.app.post('/api/orders', json=data)
        self.assertEqual(response.status_code, 200)
        response_data = response.get_json()
        expected_price = str(50 * 31)
        self.assertEqual(response_data['price'], expected_price)
        self.assertEqual(response_data['currency'], 'TWD')

if __name__ == '__main__':
    unittest.main()
