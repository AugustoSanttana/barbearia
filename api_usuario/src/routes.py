from src.application.controllers.user_controller import UserController
from flask import jsonify, make_response
from flask import Blueprint

barbearia_bp = Blueprint("barbearia", __name__)


@barbearia_bp.route("/usuario/<int:idUser>", methods=["GET"])
def get_user(idUser):
    return UserController.get_user(idUser)
    
@barbearia_bp.route("/cadastrar", methods=["POST"])
def register_user():
    return UserController.register_user()
