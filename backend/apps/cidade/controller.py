from http import HTTPStatus

from .models import CidadeModel


class CidadeController:
    @classmethod
    def get_cidades(cls):
        cidades = CidadeModel.query.all()
        cidades_json = [cidade.json for cidade in cidades]
        return cidades_json, HTTPStatus.OK

    @classmethod
    def get_cidade_by_ibge(cls, ibge):
        cidade = CidadeModel.find_by_ibge(ibge)
        if cidade:
            return cidade.json, HTTPStatus.OK
        return {'message': 'Cidade not found'}, HTTPStatus.NOT_FOUND

    @classmethod
    def add_cidade(cls, ibge, cidade, uf, ddd):
        cidade_exists = CidadeModel.find_by_ibge(ibge)
        if cidade_exists:
            return {'message': f'Cidade with IBGE {ibge} already exists'}, HTTPStatus.UNAUTHORIZED

        new_cidade = CidadeModel(ibge, cidade, uf, ddd)
        try:
            new_cidade.save()
        except Exception:
            return {'message': 'An internal error occurred.'}, HTTPStatus.INTERNAL_SERVER_ERROR

        return new_cidade.json, HTTPStatus.CREATED

    @classmethod
    def update_cidade(cls, ibge, cidade, uf, ddd):
        cidade_exists = CidadeModel.find_by_ibge(ibge)
        if not cidade_exists:
            return {'message': 'Cidade not found'}, HTTPStatus.NOT_FOUND

        cidade_exists.update(ibge, cidade, uf, ddd)

        return {'message': 'Cidade updated successfully'}, HTTPStatus.OK

    @classmethod
    def delete_cidade(cls, ibge):
        cidade = CidadeModel.find_by_ibge(ibge)
        if not cidade:
            return {'message': 'Cidade not found'}, HTTPStatus.NOT_FOUND

        cidade.delete()

        return {'message': 'Cidade deleted successfully'}, HTTPStatus.OK
