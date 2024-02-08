from flask import Blueprint, jsonify, request
from app.services import user_service
from app.extensions import jwt
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from werkzeug.exceptions import BadRequest
from sqlalchemy.exc import IntegrityError

routesBP = Blueprint('routes', __name__, url_prefix="/")

@routesBP.route('/Users', methods=['GET'])
def getUsers():
    users = user_service.getUsers()
    return jsonify(users), 200

@routesBP.route('/User', methods=['GET'])
@jwt_required()
def getUser():
    try:
        userEmail = request.args.get('email')
        if not userEmail:
            raise BadRequest
        user = user_service.getUser(userEmail)
        return jsonify(user), 200
    except TypeError:
        return jsonify({"message": "User was not found"}), 404
    except BadRequest:
        return jsonify({"message": "Invalid input"}), 400
    

@routesBP.route('/Users', methods=['POST'])
def create_user():
    try:
        data = request.json
        name = data.get('name')
        email = data.get('email')
        password = data.get('password')
        if 'name' not in data or 'email' not in data or 'password' not in data:
            raise BadRequest
        user = user_service.createUser(name, email, password)
        return jsonify(user), 200
    except BadRequest:
        return jsonify({"message": "Invalid input"}), 400
    except IntegrityError:
        return jsonify({"message": "Email already exists"}), 401

@routesBP.route('/User', methods=['PUT'])
@jwt_required()
def change_user():
    try:
        data = request.json
        email = data.get('email')
        name = data.get('name')
        if 'email' not in data or 'name' not in data:
            raise BadRequest
        user = user_service.updateUser(email, name)
        return jsonify(user), 200
    except TypeError:
        return jsonify({'message': 'User not found'}), 404
    except BadRequest:
        return jsonify({"message": "Invalid input"}), 400

@routesBP.route('/User', methods=['DELETE'])
@jwt_required()
def delete_user():
    try:
        userEmail = request.args.get('email')
        if not userEmail:
            raise BadRequest
        user_service.deleteUser(userEmail)
        return jsonify({'message': 'User deleted'}), 200
    except TypeError:
        return jsonify({'message': 'User not found'}), 404
    except BadRequest:
        return jsonify({"message": "Invalid input"}), 400

@routesBP.route('/Users', methods=['DELETE'])
def reset_users():
    user_service.deleteUsers()
    return jsonify({'message': 'Table reset'}), 200

@routesBP.route('/login', methods=['POST'])
def login():
    try:
        data = request.json
        if 'email' not in data or 'password' not in data:
            raise BadRequest
        email = data.get('email')
        password = data.get('password') 
        user = user_service.getUser(email)
        if user_service.checkUserPassword(user['password'], password):
            access_token = create_access_token(identity=user['email'])
            return jsonify({'message': f"Hello {user['name']}, you are logged in!", 'token': access_token}), 200
        else:
            return jsonify({"message": "Invalid password"}), 400
    except TypeError:
        return jsonify({"message": "User was not found"}), 404
    except BadRequest:
        return jsonify({"message": "Invalid input"}), 400