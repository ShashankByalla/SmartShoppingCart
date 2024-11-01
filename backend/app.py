from flask import Flask, jsonify, request
from flask_cors import CORS
from database import create_database, Session  # Ensure you have these defined
from models import Item  # Ensure this imports the Item model correctly

app = Flask(__name__)
CORS(app)

# Create the database
create_database()
@app.route('/')
def home():
    return "Welcome to the Smart Shopping Cart API!"

@app.route('/items', methods=['GET'])
def get_items():
    session = Session()
    items = session.query(Item).all()
    return jsonify([{ "id": item.id, "name": item.name, "price": item.price, "weight": item.weight } for item in items])

@app.route('/add_item', methods=['POST'])
def add_item():
    session = Session()
    item_data = request.json
    item = Item(name=item_data['name'], price=item_data['price'], weight=item_data['weight'])
    session.add(item)
    session.commit()
    return jsonify({"message": "Item added!"}), 201

if __name__ == '__main__':
    app.run(debug=True)
