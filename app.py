from flask import Flask, jsonify, request
from pymongo import MongoClient
from bson import ObjectId
from dotenv import load_dotenv
import os
import json
from flask_restful import Resource, Api
from waitress import serve


load_dotenv()
app = Flask(__name__)
api = Api(app)


# MongoDB connection
uri = f"mongodb+srv://{os.getenv('MONGO_USERNAME')}:{os.getenv('MONGO_PASSWORD')}@clusterappp.8u8wffp.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(uri)
db = client['clusterapp']
collection = db['users']

# User class to represent the MongoDB documents
class User:
    def __init__(self, name, email, password):
        self.id = str(ObjectId())  
        self.name = name
        self.email = email
        self.password = password

# Resource for retrieving all users
class UsersResource(Resource):
    def get(self):
        users = collection.find()
        return jsonify(json.loads(json.dumps(list(users))))

    def post(self):
        data = request.get_json()

        # handling missing fields
        if 'name' not in data or 'email' not in data or 'password' not in data:
            return jsonify({'message': 'Missing required fields'})

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
            return jsonify({'message': 'Data inserted successfully'})
        except Exception as e:
            return jsonify({'message': 'Failed to insert data', 'error': str(e)})

# Resource for retrieving a single user by ID
class UserResource(Resource):
    def get(self, id):
        try:        
            result = collection.find_one({'_id': id})
            return jsonify(result)
        except Exception as e:
            return jsonify({'message':'no user found'})
    def put(self, id):
        data = request.get_json()

        # Validate that at least one field is present for update
        if not any(field in data for field in ['name', 'email', 'password']):
            return jsonify({'message': 'No update fields provided'})

        try:
            result = collection.update_one({'_id': id}, {'$set': data})
            if result.modified_count > 0:
                return jsonify({'message': 'User updated successfully'})
            else:
                return jsonify({'message': 'User not found'})
        except Exception as e:
            return jsonify({'message': 'Failed to update user', 'error': str(e)})

    def delete(self, id):
        try:
            result = collection.delete_one({'_id': id})
            if result.deleted_count > 0:
                return jsonify({'message': 'User deleted successfully'})
            else:
                return jsonify({'message': 'User not found'})
        except Exception as e:
            return jsonify({'message': 'Failed to delete user', 'error': str(e)})

# Add resources to the API
api.add_resource(UsersResource, '/users')
api.add_resource(UserResource, '/users/<string:id>')

if __name__ == '__main__':
    #app.run(port=5005)
    serve(app, host="0.0.0.0", port=5005) #WSGI server
