from flask import Flask
from src.config.data_base import db
from src.routes import user_routes  # ou apenas routes dependendo de como está
import os
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    CORS(app) 
    # configuração do banco
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv(
        "DATABASE_URL",
        "sqlite:///db.sqlite3"  # default se não tiver variável
    )
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # inicializa o banco com o app
    db.init_app(app)

    # registra as rotas
    app.register_blueprint(user_routes, url_prefix="/user_routes")

    return app

if __name__ == "__main__":
    app = create_app()
    with app.app_context():
        db.create_all()  # garante que as tabelas existam
    app.run(debug=True)