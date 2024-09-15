from flask import Flask, request, jsonify
from validators.order_validator import OrderValidator
from services.order_service import OrderService
from models.order import Order
from models.address import Address

app = Flask(__name__)

@app.route('/api/orders', methods=['POST'])
def create_order():
    data = request.get_json()

    address_data = data.get('address', {})
    address = Address(
        city=address_data.get('city'),
        district=address_data.get('district'),
        street=address_data.get('street')
    )

    order = Order(
        id=data.get('id'),
        name=data.get('name'),
        address=address,
        price=data.get('price'),
        currency=data.get('currency')
    )

    validator = OrderValidator(order)
    validation_errors = validator.validate()

    if validation_errors:
        return jsonify({'errors': validation_errors}), 400

    service = OrderService(order)
    try:
        transformed_order = service.process_order()
        return jsonify({
            'id': transformed_order.id,
            'name': transformed_order.name,
            'address': transformed_order.address.to_dict(),
            'price': transformed_order.price,
            'currency': transformed_order.currency
        }), 200
    except ValueError as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
