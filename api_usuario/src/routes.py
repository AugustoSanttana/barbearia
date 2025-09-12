from src.application.controllers.user_controller import UserController
from flask import jsonify, make_response
from flask import Blueprint


user_routes = Blueprint("user_routes", __name__)


@user_routes.route("/usuario/<int:idUser>", methods=["GET"])
def get_user(idUser):
    return UserController.get_user(idUser)
    
@user_routes.route("/cadastrar", methods=["POST"])
def register_user():
    return UserController.register_user()
