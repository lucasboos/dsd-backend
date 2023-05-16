from http import HTTPStatus
import requests

from ..utils import validate_cep_fields, validate_cidade_fields


class CEPController:
    @classmethod
    def get_cidade(cls, ibge):
        try:
            response = requests.get(f'http://127.0.0.1:5000/localidade/{ibge}')
            response.raise_for_status()

            data = response.json()
            if data.get('mensagem'):
                return {'message': data['mensagem']}, response.status_code
            return data, response.status_code
        except requests.exceptions.RequestException as e:
            return {'message': 'Error occurred during request'}, HTTPStatus.INTERNAL_SERVER_ERROR

    @classmethod
    def get_cep(cls, ibge, cep):
        try:
            response = requests.get(f'http://127.0.0.1:5000/localidade/{ibge}/{cep}')
            response.raise_for_status()

            data = response.json()
            if data.get('mensagem'):
                return {'message': data['mensagem']}, response.status_code
            return data, response.status_code
        except requests.exceptions.RequestException as e:
            return {'message': 'Error occurred during request'}, HTTPStatus.INTERNAL_SERVER_ERROR

    @classmethod
    def add_cep(cls, cep, logradouro, ibge, bairro, cidade, uf, ddd):
        payload = {
            'cep': cep,
            'logradouro': logradouro,
            'ibge': ibge,
            'bairro': bairro,
            'cidade': cidade,
            'uf': uf,
            'ddd': ddd
        }

        validation, payload = validate_cep_fields(payload)
        if validation is not True:
            return {'message': validation}, HTTPStatus.BAD_REQUEST

        try:
            response = requests.post('http://127.0.0.1:5000/localidade', json=payload)
            response.raise_for_status()

            data = response.json()
            return {'message': data['mensagem']}, response.status_code
        except requests.exceptions.RequestException as e:
            return {'message': 'Error occurred during request'}, HTTPStatus.INTERNAL_SERVER_ERROR

    @classmethod
    def update_cidade(cls, ibge, cidade, uf, ddd):
        payload = {
            'cidade': cidade,
            'uf': uf,
            'ddd': ddd
        }

        validation, payload = validate_cidade_fields(payload)
        if validation is not True:
            return {'message': validation}, HTTPStatus.BAD_REQUEST

        try:
            response = requests.put(f'http://127.0.0.1:5000/localidade/{ibge}', json=payload)
            response.raise_for_status()

            data = response.json()
            return {'message': data['mensagem']}, response.status_code
        except requests.exceptions.RequestException as e:
            return {'message': 'Error occurred during request'}, HTTPStatus.INTERNAL_SERVER_ERROR

    @classmethod
    def delete_cidade(cls, ibge):
        try:
            response = requests.delete(f'http://127.0.0.1:5000/localidade/{ibge}')
            response.raise_for_status()

            data = response.json()
            if data.get('mensagem'):
                return {'message': data['mensagem']}, response.status_code
            return data, response.status_code
        except requests.exceptions.RequestException as e:
            return {'message': 'Error occurred during request'}, HTTPStatus.INTERNAL_SERVER_ERROR
