from src.application.controllers.user_controller import UserController
from src.application.controllers.agendamento_controller import AgendamentoController
from flask import jsonify, make_response
from flask import Blueprint


user_routes = Blueprint("user_routes", __name__)
agendamento_routes = Blueprint("agendamento_routes", __name__)


@user_routes.route("/usuario/<int:idUser>", methods=["GET"])
def get_user(idUser):
    return UserController.get_user(idUser)
    
@user_routes.route("/cadastrar", methods=["POST"])
def register_user():
    return UserController.register_user()

@user_routes.route("/login", methods=["POST"])
def login():
    return UserController.login()

#-------------------------------------#


@agendamento_routes.route("/agendamentos", methods=["GET"])
def listar_agendamentos():
    return AgendamentoController.listar_agendamentos()

@agendamento_routes.route("/agendamento", methods=["POST"])
def criar_agendamento():
    return AgendamentoController.criar_agendamento()

@agendamento_routes.route("/agendamentos/<int:id>/cancelar", methods=["PUT"])
def cancelar_agendamento(id):
    return AgendamentoController.cancelar_agendamento(id)

@agendamento_routes.route("/agendamentos/<int:id>/concluir", methods=["PUT"])
def concluir_agendamento(id):
    return AgendamentoController.concluir_agendamento(id)