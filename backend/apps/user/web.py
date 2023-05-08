from flask import Blueprint, request, jsonify
from flask_cors import CORS
from flask_jwt_extended import jwt_required

from http import HTTPStatus

from .controller import UserController, Login
from ..utils import expect


user_api_v1 = Blueprint(
    'auth_api_v1', 'auth_api_v1', url_prefix='/api/v1/user')

CORS(user_api_v1)


@user_api_v1.route('/', methods=['GET'])
@jwt_required()
def api_get_users():
    try:
        response, status = UserController.get_users()

        return jsonify(response), status
    except Exception as e:
        return jsonify({'error': str(e)}), HTTPStatus.BAD_REQUEST


@user_api_v1.route('/<email>', methods=['GET'])
def api_get_user(email):
    try:
        response, status = UserController.get_user_by_email(email)

        if response:
            return jsonify(response), status
        return jsonify(response), status
    except Exception as e:
        return jsonify({'error': str(e)}), HTTPStatus.BAD_REQUEST


@user_api_v1.route('/signup', methods=['POST'])
def api_post_user():
    req = request.get_json()

    try:
        email = expect(req.get('email'), str, 'email')
        password = expect(req.get('password'), str, 'password')

        response, status = UserController.add_user(email=email, password=password)

        return jsonify(response), status
    except Exception as e:
        return jsonify({'error': str(e)}), HTTPStatus.BAD_REQUEST


#TODO: Verificar com front se precisa mesmo
@user_api_v1.route('/<email>', methods=['PUT'])
#@jwt_required()
def api_update_user(email):
    req = request.get_json()

    try:
        new_email = expect(req.get('new_email'), str, 'new_email')
        new_password = expect(req.get('new_password'), str, 'new_password')

        response, status = UserController.update_user(email, new_email, new_password)

        return jsonify(response), status
    except Exception as e:
        return jsonify({'error': str(e)}), HTTPStatus.BAD_REQUEST


#TODO: Verificar com front se precisa mesmo
@user_api_v1.route('/<email>', methods=['DELETE'])
#@jwt_required()
def api_delete_user(email):
    try:
        response, status = UserController.delete_user(email)

        return jsonify(response), status
    except Exception as e:
        return jsonify({'error': str(e)}), HTTPStatus.BAD_REQUEST


@user_api_v1.route('/signin', methods=['POST'])
def api_signin_user():
    req = request.get_json()

    try:
        email = expect(req.get('email'), str, 'email')
        password = expect(req.get('password'), str, 'password')

        response, status = Login.login(email, password)

        return jsonify(response), status
    except Exception as e:
        return jsonify({'error': str(e)}), HTTPStatus.BAD_REQUEST
