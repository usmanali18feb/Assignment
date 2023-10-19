# Import necessary libraries and models
from flask import Flask, request, jsonify

app = Flask(__name)

# Example product data (replace with your data source)
products = [
    {
        'id': 1,
        'name': 'Product A',
        'description': 'Sample product A',
        'category': 'Category X',
        'price': 19.99,
        'in_stock': True,
    },
    {
        'id': 2,
        'name': 'Product B',
        'description': 'Sample product B',
        'category': 'Category Y',
        'price': 29.99,
        'in_stock': False,
    },
]

# Read a single product by ID
@app.route('/products/<int:product_id>', methods=['GET'])
def read_product(product_id):
    product = next((p for p in products if p['id'] == product_id), None)
    if product is not None:
        return jsonify(product)
    return 'Product not found', 404

# Update a single product by ID
@app.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    data = request.get_json()
    product = next((p for p in products if p['id'] == product_id), None)
    if product is not None:
        product.update(data)
        return jsonify(product)
    return 'Product not found', 404

# Delete a single product by ID
@app.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    product = next((p for p in products if p['id'] == product_id), None)
    if product is not None:
        products.remove(product)
        return 'Product deleted', 204
    return 'Product not found', 404

# List all products
@app.route('/products', methods=['GET'])
def list_all_products():
    return jsonify(products)

# List products by name
@app.route('/products/name/<string:product_name>', methods=['GET'])
def list_products_by_name(product_name):
    filtered_products = [p for p in products if p['name'].lower().find(product_name.lower()) != -1]
    return jsonify(filtered_products)

# List products by category
@app.route('/products/category/<string:category>', methods=['GET'])
def list_products_by_category(category):
    filtered_products = [p for p in products if p['category'] == category]
    return jsonify(filtered_products)

# List products by availability
@app.route('/products/availability/<bool:availability>', methods=['GET'])
def list_products_by_availability(availability):
    filtered_products = [p for p in products if p['in_stock'] == availability]
    return jsonify(filtered_products)

if __name__ == '__main__':
    app.run(debug=True)
