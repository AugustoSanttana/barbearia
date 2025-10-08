from flask import jsonify, request
from src.infrastructure.model_agendamento import Agendamento
from src.config.data_base import db
from datetime import datetime, date
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
            hora=datetime.strptime(hora_agenda, "%H:%M").time(),
            status="pendente"
        )

        db.session.add(agendamento)
        db.session.commit()

        return jsonify({"mensagem": "Agendamento criado com sucesso!"}), 201



    @staticmethod
    @verificar_token
    def listar_agendamentos():
        user_id = request.user_id
        is_admin = getattr(request, "is_admin", False)

        if is_admin:
            agendamentos = Agendamento.query.all()
        else:
            agendamentos = Agendamento.query.filter_by(cliente_id=user_id).all()

        for ag in agendamentos:
            if ag.data < date.today() and ag.status == "pendente":
                ag.status = "cancelado"

        db.session.commit()

        resultado = []
        for a in agendamentos:
            resultado.append({
                "id": a.id,
                "cliente_id": a.cliente_id,
                "cliente_nome": a.cliente.nome if hasattr(a, "cliente") else None,
                "profissional": a.profissional,
                "servico": a.servico,
                "data": a.data.strftime("%Y-%m-%d"),
                "hora": a.hora.strftime("%H:%M"),
                "status": a.status
            })
        return jsonify(resultado), 200



    @staticmethod
    @verificar_token
    def cancelar_agendamento(id):
        user_id = request.user_id
        agendamento = Agendamento.query.get(id)

        if not agendamento:
            return jsonify({"erro": "Agendamento não encontrado"}), 404

        if agendamento.cliente_id != user_id:
            return jsonify({"erro": "Você não tem permissão para cancelar este agendamento."}), 403

        if agendamento.status != "pendente":
            return jsonify({"erro": "Agendamento já foi concluído ou cancelado"}), 400

        agendamento.status = "cancelado"
        db.session.commit()
        return jsonify({"mensagem": "Agendamento cancelado com sucesso!"}), 200



    @staticmethod
    @verificar_token
    # token de adm
    def concluir_agendamento(id):
        if not getattr(request, "is_admin", False):
            return jsonify({"erro": "Acesso negado. Apenas administradores podem concluir agendamentos."}), 403

        agendamento = Agendamento.query.get(id)
        if not agendamento:
            return jsonify({"erro": "Agendamento não encontrado"}), 404

        if agendamento.status != "pendente":
            return jsonify({"erro": "Agendamento já foi concluído ou cancelado"}), 400

        agendamento.status = "concluido"
        db.session.commit()
        return jsonify({"mensagem": "Agendamento concluído com sucesso!"}), 200
