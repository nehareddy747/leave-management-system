from flask import Blueprint, request, jsonify
from app.models.user_model import User
import jwt
import datetime
from app.config import Config
from app.utils.decorators import token_required

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    if not data or not data.get('name') or not data.get('email') or not data.get('password'):
        return jsonify({"message": "Missing required fields"}), 400

    if User.find_by_email(data['email']):
        return jsonify({"message": "User already exists"}), 400

    role = data.get('role', 'employee').lower()
    if role not in ['employee', 'employer']:
        role = 'employee'

    User.create_user(data['name'], data['email'], data['password'], role)
    return jsonify({"message": "User created successfully"}), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    if not data or not data.get('email') or not data.get('password'):
        return jsonify({"message": "Missing required fields"}), 400

    user = User.find_by_email(data['email'])
    if not user or not User.verify_password(user['password'], data['password']):
        return jsonify({"message": "Invalid email or password"}), 401

    token = jwt.encode({
        "user_id": str(user['_id']),
        "role": user['role'],
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=24)
    }, Config.SECRET_KEY, algorithm="HS256")

    return jsonify({
        "token": token,
        "user": {
            "id": str(user['_id']),
            "name": user['name'],
            "email": user['email'],
            "role": user['role']
        }
    }), 200

@auth_bp.route('/me', methods=['GET'])
@token_required
def get_me(current_user):
    return jsonify({
        "id": str(current_user['_id']),
        "name": current_user['name'],
        "email": current_user['email'],
        "role": current_user['role']
    }), 200
