from flask_jwt_extended import create_access_token
import bcrypt

from http import HTTPStatus

from .models import UserModel


class UserController:
    @classmethod
    def get_users(cls):
        users = UserModel.get_users()
        users_json = [user.json for user in users]
        return users_json, HTTPStatus.OK

    @classmethod
    def get_user_by_email(cls, email):
        user = UserModel.find_user_by_email(email)
        if user:
            return user.json, HTTPStatus.OK
        return {'message': 'User not found'}, HTTPStatus.NOT_FOUND

    @classmethod
    def add_user(cls, email, password):
        user, status = cls.get_user_by_email(email)
        if status == HTTPStatus.OK:
            return {'message': f'Login {email} already exists'}, HTTPStatus.UNAUTHORIZED

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

        new_email_user, status = cls.get_user_by_email(new_email)
        if status == HTTPStatus.OK:
            return {'message': f'Email {new_email} already exists'}, HTTPStatus.UNAUTHORIZED

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
        user, status = UserController.get_user_by_email(email)
        token = {}

        if status == HTTPStatus.OK and bcrypt.checkpw(password.encode('utf-8'), user['password'].encode('utf-8')):
            token['token'] = create_access_token(identity=user['email'])
            return token, status

        return {'message': 'Invalid credentials'}, HTTPStatus.UNAUTHORIZED
