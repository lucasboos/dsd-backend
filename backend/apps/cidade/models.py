from ..sql_alchemy import db


class CidadeModel(db.Model):
    __tablename__ = 'cidade'
    ibge = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    uf = db.Column(db.String(2), nullable=False)
    ddd = db.Column(db.Integer, nullable=False)

    def __init__(self, ibge, nome, uf, ddd):
        self.ibge = ibge
        self.nome = nome
        self.uf = uf
        self.ddd = ddd

    @property
    def json(self):
        return {
            'ibge': self.ibge,
            'nome': self.nome,
            'uf': self.uf,
            'ddd': self.ddd,
        }

    @classmethod
    def find_by_ibge(cls, ibge):
        return cls.query.filter_by(ibge=ibge).first()

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self, ibge, nome, uf, ddd):
        self.ibge = ibge
        self.nome = nome
        self.uf = uf
        self.ddd = ddd
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
