import pymysql
from flask import Flask
from src.config.data_base import db, init_db
from src.routes import agendamento_routes
from flask_cors import CORS
from src.routes import  agendamento_routes  

def create_app():
    app = Flask(__name__)
    CORS(app)

    # Config Banco
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:mpfg2005@localhost/barbearia_db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # --- cria banco se não existir ---
    db_name = 'barbearia_db'
    conn = pymysql.connect(host='localhost', user='root', password='mpfg2005')
    cursor = conn.cursor()
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")
    conn.commit()
    cursor.close()
    conn.close()
    # ---------------------------------

    # Inicializa o SQLAlchemy
    init_db(app)

    # Blueprints

    app.register_blueprint(agendamento_routes, url_prefix="/barbearia")

    return app
