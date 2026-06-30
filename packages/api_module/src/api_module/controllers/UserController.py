from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory data store
users = [
    {"id": 1, "name": "Brijesh K Dhaker"}, 
    {"id": 2, "name": "Neeta Dhakad"},
    {"id": 3, "name": "Keshvi Dhakad"},
    {"id": 4, "name": "Tejas Dhakad"}
]

# GET: Retrieve all 
# http://127.0.0.1:5000/
@app.route('/')
def hello():
    return jsonify(message="Hello, I am here to help you !!")

# GET request: Retrieve all users
# http://127.0.0.1:5000/api/users
@app.route('/api/users', methods=['GET'])
def get_users():
    return jsonify(users)

# GET request: Retrieve a specific user by ID
# http://127.0.0.1:5000/api/users/1
@app.route('/api/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = next((user for user in users if user["id"] == user_id), None)
    if user is None:
        return jsonify({"error": "user not found"}), 404
    return jsonify(user)

# POST request: Create a new user
@app.route('/api/users', methods=['POST'])
def create_user():
    new_user = {"id": len(users) + 1, "name": request.json.get('name')}
    users.append(new_user)
    return jsonify(new_user), 201

# PUT request: Update an existing user
@app.route('/api/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = next((user for user in users if user["id"] == user_id), None)
    if user is None:
        return jsonify({"error": "user not found"}), 404
    user['name'] = request.json.get('name', user['name'])
    return jsonify(user)

# DELETE request: Delete an user
# http://127.0.0.1:5000/api/users/1
@app.route('/api/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    global users
    users = [user for user in users if user["id"] != user_id]
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)