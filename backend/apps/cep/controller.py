from http import HTTPStatus

from .models import CEPModel


class CEPController:
    @classmethod
    def get_ceps(cls):
        ceps = CEPModel.query.all()
        ceps_json = [cep.json for cep in ceps]
        return ceps_json, HTTPStatus.OK

    @classmethod
    def get_cep_by_cep(cls, cep):
        cep = CEPModel.find_by_cep(cep)
        if cep:
            return cep.json, HTTPStatus.OK
        return {'message': 'CEP not found'}, HTTPStatus.NOT_FOUND

    @classmethod
    def add_cep(cls, cep, logradouro, ibge, bairro):
        cep_exists = CEPModel.find_by_cep(cep)
        if cep_exists:
            return {'message': f'CEP {cep} already exists'}, HTTPStatus.UNAUTHORIZED

        new_cep = CEPModel(cep, logradouro, ibge, bairro)

        try:
            new_cep.save()
        except Exception:
            return {'message': 'An internal error occurred.'}, HTTPStatus.INTERNAL_SERVER_ERROR

        return new_cep.json, HTTPStatus.CREATED

    @classmethod
    def update_cep(cls, cep, logradouro, ibge, bairro):
        cep_exists = CEPModel.find_by_cep(cep)
        if not cep_exists:
            return {'message': 'CEP not found'}, HTTPStatus.NOT_FOUND

        cep_exists.update(cep, logradouro, ibge, bairro)

        return {'message': 'CEP updated successfully'}, HTTPStatus.OK

    @classmethod
    def delete_cep(cls, cep):
        cep = CEPModel.find_by_cep(cep)
        if not cep:
            return {'message': 'CEP not found'}, HTTPStatus.NOT_FOUND

        cep.delete()

        return {'message': 'CEP deleted successfully'}, HTTPStatus.OK
