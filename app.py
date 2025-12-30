from flask import Flask, jsonify, request

app = Flask(__name__)

products = [
    {
        "id": 1,
        "title": 'Product 1',
        "price": 150
    },
    {
        "id": 2,
        "title": 'Product 2',
        "price": 400
    }
]
# print(type(products))

next_id = len(products) + 1

def get_next_id():
    global next_id
    next_id += 1
    return next_id - 1

@app.route('/')
def hello():
    return '<h1>Hello World!, Goodbye!</h1>'

# if __name__ == "__main__":
#     app.run(debug=True)

@app.route('/second')
def another_route():
    return('<h2> This is another route!</h2>')

@app.route('/products')
def all_products():
    return jsonify(products)

# Get product with id == 1
# @app.route('/products/1')
# Hardcode
# def product_1():
#     return products[0]

# Same results with filter + lambda # Alternative == list comprehension

@app.route('/products/<int:id>')
def one_product(id):
    # print(type(id)) # DEBUG
    filtered_products = list(filter(lambda p: p['id'] == id, products))
    # print(list(filtered_products)) # DEBUG
    return filtered_products[0]

# POST /products (create a new product)
@app.route('/products', methods=['POST'])
def create_product():
    # print('Called create_product')
    # print(request.headers)
    # print(type(request.get_json()))
    global next_id
    product = request.get_json()
    product['id'] = get_next_id()
    products.append(product)
    return product

@app.route('/can-vote')
def can_vote():
    age = int(request.args.get('age'))
    # age = 14
    if age >= 18:
        return {"message": 'You can Vote!', "can_vote": True}
    else:
        return {"message": 'Not old enough to vote!', "can_vote": False}
