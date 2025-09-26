from flask import jsonify, request
from src.infrastructure.model_agendamento import Agendamento
from src.config.data_base import db
from datetime import datetime

class AgendamentoController:

    @staticmethod
    def criar_agendamento():
        data = request.get_json()

        cliente = data.get("cliente")
        profissional = data.get("profissional")
        servico = data.get("servico")
        data_agenda = data.get("data")  # formato "YYYY-MM-DD"
        hora_agenda = data.get("hora")  # formato "HH:MM"

        # Verifica conflito de horário com o mesmo profissional
        conflito = Agendamento.query.filter_by(
            profissional=profissional,
            data=datetime.strptime(data_agenda, "%Y-%m-%d").date(),
            hora=datetime.strptime(hora_agenda, "%H:%M").time()
        ).first()

        if conflito:
            return jsonify({"erro": "Esse horário já está ocupado!"}), 400

        agendamento = Agendamento(
            cliente=cliente,
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
                "cliente": a.cliente,
                "profissional": a.profissional,
                "servico": a.servico,
                "data": a.data.strftime("%Y-%m-%d"),
                "hora": a.hora.strftime("%H:%M")
            })
        return jsonify(resultado)
