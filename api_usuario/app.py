from flask import Flask

def create_app():
    app = Flask(__name__)

    from src.routes import barbearia_bp
    app.register_blueprint(barbearia_bp, url_prefix="/barbearia")
    return app

if __name__ == "__main__":
    print(">>> Iniciando a aplicação Flask...")
    app = create_app()
    app.run(debug=True)