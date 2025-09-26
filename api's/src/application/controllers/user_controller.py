from flask import request, jsonify, make_response
from src.application.service.user_service import UserService
from flask import request, jsonify
from src.infrastructure.model_usuario import Usuario
from src.config.data_base import db
from werkzeug.security import check_password_hash
from src.config.auth import gerar_token


class UserController:
    @staticmethod
    def register_user():
        data = request.get_json()
        nome = data.get('nome')
        email = data.get('email')
        senha = data.get('senha')
        cpf = data.get('cpf')
        endereco = data.get('endereco')

        if not nome or not email or not senha or not cpf or not endereco:
            return make_response(jsonify({"erro": "Campos obrigatórios ausentes"}), 400)
        
        user = UserService.create_user(nome, email, senha, cpf, endereco)
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
    
    @staticmethod
    def login():
        data = request.get_json()
        email = data.get("email")
        senha = data.get("senha")

        usuario = UserService.login(email, senha)
        if not usuario:
            return jsonify({"erro": "Credenciais inválidas"}), 401

        token = gerar_token(usuario.id)
        return jsonify({"token": token})