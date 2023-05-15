from http import HTTPStatus
import requests

from utils import validate_user_fields


class UserController:
    @classmethod
    def get_users(cls):
        users = UserModel.get_users()
        users_json = [user.json for user in users]
        return users_json, HTTPStatus.OK

    @classmethod
    def get_user_by_login(cls, login):
        user = UserModel.find_user_by_login(login)
        if user:
            return user.json, HTTPStatus.OK
        return {'message': 'User not found'}, HTTPStatus.NOT_FOUND

    @classmethod
    def add_user(cls, nome, login, cep, numero=None, complemento=None, telefone=None):
        payload = {
            'nome': nome,
            'login': login,
            'cep': cep,
            'numero': numero,
            'complemento': complemento,
            'telefone': telefone
        }

        validation, payload = validate_user_fields(payload)
        if validation is not True:
            return {'message': validation}, HTTPStatus.BAD_REQUEST

        try:
            response = requests.post('http://127.0.0.1:5000/usuario', json=payload)
            if response.status_code == 200:
                dados = response.json()
                return dados
            else:
                print("Erro na requisição:", response.status_code)
        except requests.exceptions.RequestException as e:
            print("Ocorreu um erro na requisição:", e)

    @classmethod
    def update_user(cls, login, new_nome, new_login, new_cep, new_numero=None, new_complemento=None, new_telefone=None):
        user = UserModel.find_user_by_login(login)
        if not user:
            return {'message': 'User not found'}, HTTPStatus.NOT_FOUND

        if new_login != login:
            existing_user = UserModel.find_user_by_login(new_login)
            if existing_user:
                return {'message': f'Login {new_login} already exists'}, HTTPStatus.UNAUTHORIZED

        user.update_user(new_nome, new_login, new_cep, new_numero, new_complemento, new_telefone)

        try:
            user.save_user()
        except Exception:
            return {'message': 'An internal error occurred.'}, HTTPStatus.INTERNAL_SERVER_ERROR

        return {'message': 'User updated successfully'}, HTTPStatus.OK

    @classmethod
    def delete_user(cls, login):
        user = UserModel.find_user_by_login(login)
        if not user:
            return {'message': 'User not found'}, HTTPStatus.NOT_FOUND

        user.delete_user()

        return {'message': 'User deleted successfully'}, HTTPStatus.OK
