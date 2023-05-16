from flask import Blueprint, request, jsonify
from flask_cors import CORS

from http import HTTPStatus

from .controller import CEPController
from ..utils import expect

cep_api_v1 = Blueprint('cep_api_v1', 'cep_api_v1', url_prefix='/api/v1/cep')
CORS(cep_api_v1)


@cep_api_v1.route('/cidade/<ibge>', methods=['GET'])
def api_get_cidade(ibge):
    try:
        response, status = CEPController.get_cidade(ibge)

        return jsonify(response), status
    except Exception as e:
        return jsonify({'error': str(e)}), HTTPStatus.BAD_REQUEST


@cep_api_v1.route('/<ibge>/<cep>', methods=['GET'])
def api_get_cep(ibge, cep):
    try:
        response, status = CEPController.get_cep(ibge, cep)

        return jsonify(response), status
    except Exception as e:
        return jsonify({'error': str(e)}), HTTPStatus.BAD_REQUEST


@cep_api_v1.route('/', methods=['POST'])
def api_post_cep():
    req = request.get_json()

    try:
        cep = req.get('cep')
        logradouro = req.get('logradouro')
        ibge = req.get('ibge')
        bairro = req.get('bairro')
        cidade =req.get('cidade')
        uf = req.get('uf')
        ddd = req.get('ddd')

        response, status = CEPController.add_cep(cep=cep, logradouro=logradouro, ibge=ibge, bairro=bairro, cidade=cidade, uf=uf, ddd=ddd)

        return jsonify(response), status
    except Exception as e:
        return jsonify({'error': str(e)}), HTTPStatus.BAD_REQUEST


@cep_api_v1.route('/<ibge>', methods=['PUT'])
def api_update_cidade(ibge):
    req = request.get_json()

    try:
        cidade =req.get('cidade')
        uf = req.get('uf')
        ddd = req.get('ddd')

        response, status = CEPController.update_cidade(ibge=ibge, cidade=cidade, uf=uf, ddd=ddd)

        return jsonify(response), status
    except Exception as e:
        return jsonify({'error': str(e)}), HTTPStatus.BAD_REQUEST


@cep_api_v1.route('/<ibge>', methods=['DELETE'])
def api_delete_cidade(ibge):
    try:
        response, status = CEPController.delete_cidade(ibge)

        return jsonify(response), status
    except Exception as e:
        return jsonify({'error': str(e)}), HTTPStatus.BAD_REQUEST
