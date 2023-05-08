from ..sql_alchemy import db


class UserModel(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50))
    password = db.Column(db.String(255))

    def __init__(self, email, password):
        self.email = email
        self.password = password

    @property
    def json(self):
        return {
            'id': self.id,
            'email': self.email,
            'password': self.password,
        }

    @classmethod
    def get_users(cls):
        return [user for user in cls.query.all()]

    @classmethod
    def find_user_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    @classmethod  
    def find_user_by_email(cls, email): 
        return cls.query.filter_by(email=email).first()

    def save_user(self):
        db.session.add(self)
        db.session.commit()

    def update_user(self, email, password):
        self.email = email
        self.password = password

    def delete_user(self):
        db.session.delete(self)
        db.session.commit()
