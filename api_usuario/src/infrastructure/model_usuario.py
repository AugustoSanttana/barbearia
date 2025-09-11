import re
from src.config.data_base import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    cpf = db.Column(db.String(11), unique=True, nullable=False)
    endereco = db.Column(db.String(100), nullable=False)


    def to_dict(self):
        return  {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "password": self.password,
            "cpf": self.cpf,
            "endereco": self.endereco
        }