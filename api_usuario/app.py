import pymysql
from flask import Flask
from src.config.data_base import db, init_db
from src.routes import user_routes  
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    CORS(app) 

    # Configurações do SQLAlchemy
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:mpfg2005@localhost/barbearia_db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # --- CRIAR BANCO SE NÃO EXISTIR ---
    db_name = 'barbearia_db'
    conn = pymysql.connect(host='localhost', user='root', password='mpfg2005')
    cursor = conn.cursor()
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")
    conn.commit()
    cursor.close()
    conn.close()
    # -----------------------------------

    # Inicializa o SQLAlchemy
    init_db(app)

    app.register_blueprint(user_routes, url_prefix="/user_routes")

    return app

if __name__ == "__main__":
    app = create_app()
    with app.app_context():
        db.create_all()  
    app.run(debug=True)