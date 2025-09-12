from flask import Flask
from src.config.data_base import db, init_db
from src.routes import user_routes  
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    CORS(app) 
    
    init_db(app)

    app.register_blueprint(user_routes, url_prefix="/user_routes")

    return app

if __name__ == "__main__":
    app = create_app()
    with app.app_context():
        db.create_all()  
    app.run(debug=True)