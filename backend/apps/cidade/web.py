from flask import Blueprint, request, jsonify
from flask_cors import CORS
from flask_jwt_extended import jwt_required

from http import HTTPStatus

from .controller import CidadeController
from ..utils import expect

cidade_api_v1 = Blueprint('cidade_api_v1', 'cidade_api_v1', url_prefix='/api/v1/cidade')
CORS(cidade_api_v1)


@cidade_api_v1.route('/', methods=['GET'])
#@jwt_required()
def api_get_cidades():
    try:
        response, status = CidadeController.get_cidades()
        return jsonify(response), status
    except Exception as e:
        return jsonify({'error': str(e)}), HTTPStatus.BAD_REQUEST


@cidade_api_v1.route('/<ibge>', methods=['GET'])
def api_get_cidade(ibge):
    try:
        response, status = CidadeController.get_cidade_by_ibge(ibge)

        if response:
            return jsonify(response), status
        return jsonify(response), status
    except Exception as e:
        return jsonify({'error': str(e)}), HTTPStatus.BAD_REQUEST


@cidade_api_v1.route('/', methods=['POST'])
def api_post_cidade():
    req = request.get_json()

    try:
        ibge = expect(req.get('ibge'), int, 'ibge')
        nome = expect(req.get('nome'), str, 'nome')
        uf = expect(req.get('uf'), str, 'uf')
        ddd = expect(req.get('ddd'), int, 'ddd')

        response, status = CidadeController.add_cidade(ibge=ibge, nome=nome, uf=uf, ddd=ddd)

        return jsonify(response), status
    except Exception as e:
        return jsonify({'error': str(e)}), HTTPStatus.BAD_REQUEST


@cidade_api_v1.route('/<ibge>', methods=['PUT'])
def api_update_cidade(ibge):
    req = request.get_json()

    try:
        nome = expect(req.get('nome'), str, 'nome')
        uf = expect(req.get('uf'), str, 'uf')
        ddd = expect(req.get('ddd'), int, 'ddd')

        response, status = CidadeController.update_cidade(ibge=ibge, nome=nome, uf=uf, ddd=ddd)

        return jsonify(response), status
    except Exception as e:
        return jsonify({'error': str(e)}), HTTPStatus.BAD_REQUEST


@cidade_api_v1.route('/<ibge>', methods=['DELETE'])
def api_delete_cidade(ibge):
    try:
        response, status = CidadeController.delete_cidade(ibge)

        return jsonify(response), status
    except Exception as e:
        return jsonify({'error': str(e)}), HTTPStatus.BAD_REQUEST
