from flask import Flask, jsonify, request

app = Flask(__name__)
app.config.update(ENV='development')

from products import products


@app.route('/products', methods=['GET', 'POST'])
def products_list():
    # devolver todos los productos
    if request.method == 'GET':
        return jsonify(products)
    
    # crear un producto
    if request.method == 'POST':
        product = request.get_json()
        products.append(product)
        return jsonify({'message': 'Product created', 'products': products})


@app.route('/products/<string:product_name>', methods=['GET', 'PATCH', 'PUT', 'DELETE'])
def product_detail(product_name):

    if request.method == 'GET':
        products_found = []
        for product in products:
            if product['name'] == product_name:
                products_found.append(product)
                return jsonify(products_found)
        return jsonify({'message': 'Product not found'})
    
    if request.method == 'PUT':
        product_found = {}
        for product in products:
            if product['name'] == product_name:
                product_found = product
                break
        if product_found:
            product_updated = request.get_json()
            product_found['name'] = product_updated['name']
            product_found['price'] = product_updated['price']
            product_found['quantity'] = product_updated['quantity']
            return jsonify({'message': 'Product updated', 'products': products})
        return jsonify({'message': 'Product not found'})
    
    if request.method == 'DELETE':
        product_found = {}
        for product in products:
            if product['name'] == product_name:
                product_found = product
                break
        if product_found:
            products.remove(product_found)
            return jsonify({'message': 'Product deleted', 'products': products})
        return jsonify({'message': 'Product not found'})

if __name__ == '__main__':
    app.run(debug=True, port=4000)
    