from ..sql_alchemy import db


class UserModel(db.Model):
    __tablename__ = 'usuario'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(100), nullable=False)
    login = db.Column(db.String(10), nullable=False)
    cep = db.Column(db.Integer, nullable=False)
    numero = db.Column(db.Integer)
    complemento = db.Column(db.String(25))
    telefone = db.Column(db.Integer)

    def __init__(self, nome, login, cep, numero=None, complemento=None, telefone=None):
        self.nome = nome
        self.login = login
        self.cep = cep
        self.numero = numero
        self.complemento = complemento
        self.telefone = telefone

    @property
    def json(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'login': self.login,
            'cep': self.cep,
            'numero': self.numero,
            'complemento': self.complemento,
            'telefone': self.telefone,
        }

    @classmethod
    def get_users(cls):
        return [user for user in cls.query.all()]

    @classmethod  
    def find_user_by_login(cls, login): 
        return cls.query.filter_by(login=login).first()

    def save_user(self):
        db.session.add(self)
        db.session.commit()

    def update_user(self, new_nome, new_login, new_cep, new_numero=None, new_complemento=None, new_telefone=None):
        self.nome = new_nome
        self.login = new_login
        self.cep = new_cep
        self.numero = new_numero
        self.complemento = new_complemento
        self.telefone = new_telefone

    def delete_user(self):
        db.session.delete(self)
        db.session.commit()
