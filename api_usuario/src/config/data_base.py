import os
from flask_sqlalchemy import SQLAlchemy 

db = SQLAlchemy()

def init_db(app):
    # Lê a URL de conexão do banco de dados das variáveis de ambiente.
    # O valor padrão é para um banco SQLite, útil para testes locais sem Docker.
    database_url = os.getenv('DATABASE_URL', 'sqlite:///market_management.db')
    app.config['SQLALCHEMY_DATABASE_URI'] = database_url
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)