from flask import Blueprint, request, jsonify
from flask_cors import CORS

from http import HTTPStatus

from .controller import UserController


user_api_v1 = Blueprint('auth_api_v1', 'auth_api_v1', url_prefix='/api/v1/user')
CORS(user_api_v1)


@user_api_v1.route('/', methods=['GET'])
def api_get_users():
    try:
        response, status = UserController.get_users()

        return jsonify(response), status
    except Exception as e:
        return jsonify({'error': str(e)}), HTTPStatus.BAD_REQUEST
    

@user_api_v1.route('/complete', methods=['GET'])
def api_get_users_complete():
    try:
        response, status = UserController.get_users_complete()

        return jsonify(response), status
    except Exception as e:
        return jsonify({'error': str(e)}), HTTPStatus.BAD_REQUEST


@user_api_v1.route('/<id>', methods=['GET'])
def api_get_user_by_id(id):
    try:
        response, status = UserController.get_user_by_id(id)

        return jsonify(response), status
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


@user_api_v1.route('/<id>', methods=['DELETE'])
def api_delete_user(id):
    try:
        response, status = UserController.delete_user(id)

        return jsonify(response), status
    except Exception as e:
        return jsonify({'error': str(e)}), HTTPStatus.BAD_REQUEST
