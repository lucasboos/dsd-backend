from flask import Blueprint, request, jsonify
from flask_cors import CORS

from http import HTTPStatus

from .controller import UserController
from ..utils import expect


user_api_v1 = Blueprint('auth_api_v1', 'auth_api_v1', url_prefix='/api/v1/user')
CORS(user_api_v1)


@user_api_v1.route('/', methods=['GET'])
def api_get_users():
    try:
        response, status = UserController.get_users()
        return jsonify(response), status
    except Exception as e:
        return jsonify({'error': str(e)}), HTTPStatus.BAD_REQUEST


@user_api_v1.route('/<login>', methods=['GET'])
def api_get_user(login):
    try:
        response, status = UserController.get_user_by_login(login)
        if response:
            return jsonify(response), status
        return jsonify({'message': 'User not found'}), status
    except Exception as e:
        return jsonify({'error': str(e)}), HTTPStatus.BAD_REQUEST


@user_api_v1.route('/', methods=['POST'])
def api_post_user():
    req = request.get_json()

    try:
        nome = req.get('nome')
        login = req.get('login')
        cep = req.get('cep')
        numero = req.get('numero')
        complemento = req.get('complemento')
        telefone = req.get('telefone')

        response, status = UserController.add_user(nome, login, cep, numero, complemento, telefone)
        return jsonify(response), status
    except Exception as e:
        return jsonify({'error': str(e)}), HTTPStatus.BAD_REQUEST


@user_api_v1.route('/<login>', methods=['PUT'])
def api_update_user(login):
    req = request.get_json()

    try:
        new_nome = expect(req.get('new_nome'), str, 'new_nome')
        new_login = expect(req.get('new_login'), str, 'new_login')
        new_cep = expect(req.get('new_cep'), int, 'new_cep')
        new_numero = req.get('new_numero')
        new_complemento = req.get('new_complemento')
        new_telefone = req.get('new_telefone')

        response, status = UserController.update_user(login, new_nome, new_login, new_cep, new_numero, new_complemento, new_telefone)
        return jsonify(response), status
    except Exception as e:
        return jsonify({'error': str(e)}), HTTPStatus.BAD_REQUEST


@user_api_v1.route('/<login>', methods=['DELETE'])
def api_delete_user(login):
    try:
        response, status = UserController.delete_user(login)
        return jsonify(response), status
    except Exception as e:
        return jsonify({'error': str(e)}), HTTPStatus.BAD_REQUEST
