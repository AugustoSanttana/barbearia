from flask import request, jsonify
from src.config.data_base import db
from src.config.auth import verificar_token_usuario
from src.infrastructure.model_avaliacao import Avaliacao
from src.infrastructure.model_cabeleireiro import Cabeleireiro

class AvaliacaoController:

    @staticmethod
    @verificar_token_usuario
    def criar_avaliacao(user_id):
        dados = request.get_json()
        
        nota = dados.get('nota')
        comentario = dados.get('comentario')
        cabeleireiro_id = dados.get('cabeleireiro_id')

        if not nota or not cabeleireiro_id:
            return jsonify({"erro": "Nota e ID do cabeleireiro são obrigatórios"}), 400

        if not Cabeleireiro.query.get(cabeleireiro_id):
            return jsonify({"erro": "Cabeleireiro não encontrado"}), 404

        if not 1 <= int(nota) <= 5:
            return jsonify({"erro": "A nota deve ser um número entre 1 e 5"}), 400

        nova_avaliacao = Avaliacao(
            nota=nota,
            comentario=comentario,
            usuario_id=user_id, # ID do usuário vem do token
            cabeleireiro_id=cabeleireiro_id
        )

        db.session.add(nova_avaliacao)
        db.session.commit()

        return jsonify({"mensagem": "Avaliação enviada com sucesso!"}), 201