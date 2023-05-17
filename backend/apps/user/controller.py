from http import HTTPStatus
import requests

from ..utils import validate_user_fields


class UserController:
    @classmethod
    def get_user_by_id(cls, id):
        try:
            response = requests.get(f'http://127.0.0.1:5000/usuario/{id}')
            data = response.json()

            if data.get('mensagem'):
                return {'message': data['mensagem']}, response.status_code
            return data, response.status_code
        except requests.exceptions.RequestException as e:
            return {'message': 'Error occurred during request'}, HTTPStatus.INTERNAL_SERVER_ERROR

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
            data = response.json()

            return {'message': data['mensagem']}, response.status_code
        except requests.exceptions.RequestException as e:
            return {'message': 'Error occurred during request'}, HTTPStatus.INTERNAL_SERVER_ERROR
