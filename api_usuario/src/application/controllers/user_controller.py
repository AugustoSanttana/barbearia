from flask import request, jsonify, make_response
from src.application.service.user_service import UserService

class UserController:
    @staticmethod
    def register_user():
        data = request.get_json()
        name = data.get('name')
        email = data.get('email')
        password = data.get('password')
        cpf = data.get('cpf')
        endereco = data.get('endereco')

        if not name or not email or not password or not cpf or not endereco:
            return make_response(jsonify({"erro": "Campos obrigatórios ausentes"}), 400)
        
        user = UserService.create_user(name, email, password, cpf, endereco)
        return make_response(jsonify({
            "mensagem": "User salvo com sucesso",
            "usuarios": user.to_dict()
        }), 200)
    
    @staticmethod
    def get_user(idUser):
        user = UserService.get_user(idUser)
        if not user:
            return make_response(jsonify({"erro": "Usuário não encontrado"}), 404)
        return make_response(jsonify({
            "usuario": user.to_dict()
        }), 200)