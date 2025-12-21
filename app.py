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

@app.route('/can-vote')
def can_vote():
    age = int(request.args.get('age'))
    # age = 14
    if age >= 18:
        return {"message": 'You can Vote!', "can_vote": True}
    else:
        return {"message": 'Not old enough to vote!', "can_vote": False}
