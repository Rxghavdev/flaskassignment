from flask import Flask, jsonify, request
from pymongo import MongoClient     #can also use mongoengine
from bson import ObjectId
from dotenv import load_dotenv
import os
import json

load_dotenv()
app = Flask(__name__)

# MongoDB connection
uri = f"mongodb+srv://{os.getenv('MONGO_USERNAME')}:{os.getenv('MONGO_PASSWORD')}@clusterappp.8u8wffp.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(uri)
db = client['clusterapp']
collection = db['users']

# User class to represent the MongoDB documents
class User:
    def __init__(self, name, email, password):
        self.id = str(ObjectId())  # Generate a new ObjectId for each user
        self.name = name
        self.email = email
        self.password = password

# Route to test database connection
@app.route('/')
def test_connection():
    try:
        client.server_info()  # Attempt to execute a MongoDB server command
        return jsonify({'message': 'Database connected'})
    except Exception as e:
        return jsonify({'message': 'Database connection failed', 'error': str(e)}), 500

# Route to retrieve all users
@app.route('/users', methods=['GET'])
def get_data():
    users = collection.find()
    return jsonify(json.loads(json.dumps(list(users)))), 200

# Route to add a new user
@app.route('/users', methods=['POST'])
def post_users():
    data = request.get_json()

    # handling missing fields
    if 'name' not in data or 'email' not in data or 'password' not in data:
        return jsonify({'message': 'Missing required fields'}), 400

    user = User(name=data['name'], email=data['email'], password=data['password'])

    # into a dictionary to be inserted into the collection
    user_data = {
        '_id': user.id,
        'name': user.name,
        'email': user.email,
        'password': user.password
    }

    try:
        # Insert the user data into the collection
        collection.insert_one(user_data)
        return jsonify({'message': 'Data inserted successfully'}), 201
    except Exception as e:
        return jsonify({'message': 'Failed to insert data', 'error': str(e)}), 500

# Route to clear all users
@app.route('/clear_data', methods=['DELETE'])
def clear_data():
    try:
        # Delete all documents in the user collection
        collection.delete_many({})
        return jsonify({'message': 'Data cleared successfully'}), 200
    except Exception as e:
        return jsonify({'message': 'Failed to clear data', 'error': str(e)}), 500

# Route to retrieve a single user by ID
@app.route('/users/<id>', methods=['GET'])
def get_user(id):
    user = collection.find_one({'_id': id})
    if user:
        return jsonify(json.loads(json.dumps(user))), 200
    else:
        return jsonify({'message': 'User not found'}), 404

# Route to update a user by ID
@app.route('/users/<id>', methods=['PUT'])
def update_user(id):
    data = request.get_json()

    # Validate that at least one field is present for update
    if not any(field in data for field in ['name', 'email', 'password']):
        return jsonify({'message': 'No update fields provided'}), 400

    try:
        result = collection.update_one({'_id': id}, {'$set': data})
        if result.modified_count > 0:
            return jsonify({'message': 'User updated successfully'}), 200
        else:
            return jsonify({'message': 'User not found'}), 404
    except Exception as e:
        return jsonify({'message': 'Failed to update user', 'error': str(e)}), 500

# Route to delete a user by ID
@app.route('/users/<id>', methods=['DELETE'])
def delete_user(id):
    try:
        result = collection.delete_one({'_id': id})
        if result.deleted_count > 0:
            return jsonify({'message': 'User deleted successfully'}), 200
        else:
            return jsonify({'message': 'User not found'}), 404
    except Exception as e:
        return jsonify({'message': 'Failed to delete user', 'error': str(e)}), 500

if __name__ == '__main__':
    app.run()
