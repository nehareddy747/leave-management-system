from functools import wraps
from flask import request, jsonify
import jwt
from app.config import Config
from app.models.user_model import User

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if "Authorization" in request.headers:
            auth_header = request.headers["Authorization"]
            if auth_header.startswith("Bearer "):
                token = auth_header.split(" ")[1]
        
        if not token:
            return jsonify({"message": "Token is missing!"}), 401

        try:
            data = jwt.decode(token, Config.SECRET_KEY, algorithms=["HS256"])
            current_user = User.find_by_id(data["user_id"])
            if not current_user:
                return jsonify({"message": "User not found!"}), 401
        except jwt.ExpiredSignatureError:
            return jsonify({"message": "Token has expired!"}), 401
        except jwt.InvalidTokenError:
            return jsonify({"message": "Token is invalid!"}), 401
            
        return f(current_user, *args, **kwargs)
    return decorated

def employer_required(f):
    @wraps(f)
    def decorated(current_user, *args, **kwargs):
        if current_user.get("role") != "employer":
            return jsonify({"message": "Employer access required!"}), 403
        return f(current_user, *args, **kwargs)
    return decorated
