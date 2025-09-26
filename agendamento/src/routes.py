from flask import Blueprint
from src.application.controllers.agendamento_controller import AgendamentoController

agendamento_routes = Blueprint("agendamento_routes", __name__)

@agendamento_routes.route("/agendamento", methods=["POST"])
def criar_agendamento():
    return AgendamentoController.criar_agendamento()

@agendamento_routes.route("/agendamentos", methods=["GET"])
def listar_agendamentos():
    return AgendamentoController.listar_agendamentos()