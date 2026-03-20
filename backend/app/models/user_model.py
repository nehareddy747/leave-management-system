from app.db import db
from werkzeug.security import generate_password_hash, check_password_hash
from bson.objectid import ObjectId

class User:
    collection = db.users

    @staticmethod
    def create_user(name, email, password, role="employee"):
        hashed_password = generate_password_hash(password)
        user_data = {
            "name": name,
            "email": email,
            "password": hashed_password,
            "role": role
        }
        return User.collection.insert_one(user_data)

    @staticmethod
    def find_by_email(email):
        return User.collection.find_one({"email": email})

    @staticmethod
    def find_by_id(user_id):
        return User.collection.find_one({"_id": ObjectId(user_id)})
        
    @staticmethod
    def verify_password(stored_password, provided_password):
        return check_password_hash(stored_password, provided_password)
