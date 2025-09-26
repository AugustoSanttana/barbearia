from flask import jsonify, request
from src.infrastructure.model_agendamento import Agendamento
from src.config.data_base import db
from datetime import datetime
from src.config.auth import verificar_token  

class AgendamentoController:

    @staticmethod
    @verificar_token
    def criar_agendamento():
        data = request.get_json()
        cliente_id = request.user_id  
        profissional = data.get("profissional")
        servico = data.get("servico")
        data_agenda = data.get("data")
        hora_agenda = data.get("hora")

        # verificar conflito
        conflito = Agendamento.query.filter_by(
            profissional=profissional,
            data=datetime.strptime(data_agenda, "%Y-%m-%d").date(),
            hora=datetime.strptime(hora_agenda, "%H:%M").time()
        ).first()

        if conflito:
            return jsonify({"erro": "Esse horário já está ocupado!"}), 400

        agendamento = Agendamento(
            cliente_id=cliente_id,
            profissional=profissional,
            servico=servico,
            data=datetime.strptime(data_agenda, "%Y-%m-%d").date(),
            hora=datetime.strptime(hora_agenda, "%H:%M").time()
        )

        db.session.add(agendamento)
        db.session.commit()

        return jsonify({"mensagem": "Agendamento criado com sucesso!"}), 201

    @staticmethod
    def listar_agendamentos():
        agendamentos = Agendamento.query.all()
        resultado = []
        for a in agendamentos:
            resultado.append({
                "id": a.id,
                "cliente_id": a.cliente_id,
                "cliente_nome": a.cliente.nome,   
                "profissional": a.profissional,
                "servico": a.servico,
                "data": a.data.strftime("%Y-%m-%d"),
                "hora": a.hora.strftime("%H:%M")
            })
        return jsonify(resultado)
