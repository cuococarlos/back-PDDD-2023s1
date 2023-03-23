from flask import Flask, request, jsonify
from flask_pymongo import PyMongo, ObjectId
from flask_cors import CORS

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://localhost/pythonreact'
mongo = PyMongo(app)

CORS(app)

db = mongo.db.users

@app.route('/users', methods=['POST'])
def createUser():
  id = db.insert_one({
    'name': request.json['name'],
    'email': request.json['email'],
    'dni': request.json['dni']
  }).inserted_id
  return jsonify(str(ObjectId(id)))
  

@app.route('/users', methods=['GET'])
def getUsers():
    users = []
    for user in db.find():
        users.append({
            '_id': str(ObjectId(user['_id'])),
            'name': user['name'],
            'email': user['email']
        })
    return jsonify(users)

@app.route('/user/<id>', methods=['GET'])
def getUser(id):
    user = db.find_one({'_id': ObjectId(id)})
    return jsonify({
        "_id": str(ObjectId(user['_id'])),
        "name": user['name'],
        "email": user['email'],
        "dni": user['dni']
    })

@app.route('/user/<id>', methods=['delete'])
def delete(id):
    db.delete_one({'_id': ObjectId(id)})
    return jsonify({'msg': 'User deleted'})

if __name__ == "__main__":
    app.run(debug=True)