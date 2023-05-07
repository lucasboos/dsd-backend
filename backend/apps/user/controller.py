from flask_jwt_extended import create_access_token
import bcrypt

from http import HTTPStatus

from .models import UserModel


class UserController:
    @classmethod
    def get_users(cls):
        return UserModel.get_users()

    @classmethod
    def get_user_by_email(cls, email):
        user = UserModel.find_user_by_email(email)
        if user:
            return user.json
        return None

    @classmethod
    def add_user(cls, email, password):
        user = cls.get_user_by_email(email)
        if user:
            return {'message': f'Login {user["email"]} already exists'}, HTTPStatus.UNAUTHORIZED

        hash_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

        new_user = UserModel(email, hash_password)

        try:
            new_user.save_user()
        except Exception:
            return {'message': 'An internal error occurred.'}, HTTPStatus.INTERNAL_SERVER_ERROR

        return new_user.json, HTTPStatus.CREATED

    @classmethod
    def update_user(cls, email, new_email, new_password):
        user = UserModel.find_user_by_email(email)
        if not user:
            return {'message': 'User not found'}, HTTPStatus.NOT_FOUND

        user.email = new_email
        user.password = bcrypt.hashpw(new_password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        user.save_user()

        return {'message': 'User updated successfully'}, HTTPStatus.OK

    @classmethod
    def delete_user(cls, email):
        user = UserModel.find_user_by_email(email)
        if not user:
            return {'message': 'User not found'}, HTTPStatus.NOT_FOUND

        user_instance = UserModel.query.filter_by(email=email).first()
        user_instance.delete_user()

        return {'message': 'User deleted successfully'}, HTTPStatus.OK

class Login:
    @staticmethod
    def login(email, password):
        user = UserController.get_user_by_email(email)
        token = {}

        if user and bcrypt.checkpw(password.encode('utf-8'), user['password'].encode('utf-8')):
            token["token"] = create_access_token(identity=user['email'])

        return token
