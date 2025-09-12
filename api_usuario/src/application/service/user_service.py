from src.domain.user import UserDomain
from src.infrastructure.model_usuario import User
from src.config.data_base import db

class UserService:
    @staticmethod
    def create_user(name, email, password, cpf, endereco):
        new_user = UserDomain(name, email, password, cpf, endereco)
        user = User(name=new_user.name, email=new_user.email, password=new_user.password, cpf=new_user.cpf, endereco=new_user.endereco)
        db.session.add(user)
        db.session.commit()
        return user

    @staticmethod
    def get_user(idUser):
        user = User.query.get(idUser)
        if not user:
            return None
        return user

