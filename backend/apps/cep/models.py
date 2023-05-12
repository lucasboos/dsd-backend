from ..sql_alchemy import db


class CEPModel(db.Model):
    __tablename__ = 'cep'
    cep = db.Column(db.Integer, primary_key=True)
    logradouro = db.Column(db.String(100), nullable=False)
    ibge = db.Column(db.Integer, db.ForeignKey('cidade.ibge'), nullable=False)
    bairro = db.Column(db.String(25), nullable=False)

    def __init__(self, cep, logradouro, ibge, bairro):
        self.cep = cep
        self.logradouro = logradouro
        self.ibge = ibge
        self.bairro = bairro

    @property
    def json(self):
        return {
            'cep': self.cep,
            'logradouro': self.logradouro,
            'ibge': self.ibge,
            'bairro': self.bairro,
        }

    @classmethod
    def find_by_cep(cls, cep):
        return cls.query.filter_by(cep=cep).first()

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self, cep, logradouro, ibge, bairro):
        self.cep = cep
        self.logradouro = logradouro
        self.ibge = ibge
        self.bairro = bairro
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
