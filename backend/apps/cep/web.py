from flask import Blueprint, request, jsonify
from flask_cors import CORS
from flask_jwt_extended import jwt_required

from http import HTTPStatus

from .controller import CEPController
from ..utils import expect

cep_api_v1 = Blueprint('cep_api_v1', 'cep_api_v1', url_prefix='/api/v1/cep')
CORS(cep_api_v1)


@cep_api_v1.route('/', methods=['GET'])
#@jwt_required()
def api_get_ceps():
    try:
        response, status = CEPController.get_ceps()
        return jsonify(response), status
    except Exception as e:
        return jsonify({'error': str(e)}), HTTPStatus.BAD_REQUEST


@cep_api_v1.route('/<cep>', methods=['GET'])
def api_get_cep(cep):
    try:
        response, status = CEPController.get_cep_by_cep(cep)

        if response:
            return jsonify(response), status
        return jsonify(response), status
    except Exception as e:
        return jsonify({'error': str(e)}), HTTPStatus.BAD_REQUEST


@cep_api_v1.route('/', methods=['POST'])
def api_post_cep():
    req = request.get_json()

    try:
        cep = expect(req.get('cep'), int, 'cep')
        logradouro = expect(req.get('logradouro'), str, 'logradouro')
        ibge = expect(req.get('ibge'), int, 'ibge')
        bairro = expect(req.get('bairro'), str, 'bairro')

        response, status = CEPController.add_cep(cep=cep, logradouro=logradouro, ibge=ibge, bairro=bairro)

        return jsonify(response), status
    except Exception as e:
        return jsonify({'error': str(e)}), HTTPStatus.BAD_REQUEST


@cep_api_v1.route('/<cep>', methods=['PUT'])
def api_update_cep(cep):
    req = request.get_json()

    try:
        cep = expect(req.get('cep'), int, 'cep')
        logradouro = expect(req.get('logradouro'), str, 'logradouro')
        ibge = expect(req.get('ibge'), int, 'ibge')
        bairro = expect(req.get('bairro'), str, 'bairro')

        response, status = CEPController.update_cep(cep=cep, logradouro=logradouro, ibge=ibge, bairro=bairro)

        return jsonify(response), status
    except Exception as e:
        return jsonify({'error': str(e)}), HTTPStatus.BAD_REQUEST


@cep_api_v1.route('/<cep>', methods=['DELETE'])
def api_delete_cep(cep):
    try:
        response, status = CEPController.delete_cep(cep)

        return jsonify(response), status
    except Exception as e:
        return jsonify({'error': str(e)}), HTTPStatus.BAD_REQUEST
