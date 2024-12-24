from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config import Config

# inicializa o SQLALchemy
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # inicializa o banco de dados no app
    db.init_app(app)

    # Registra as rotas
    with app.app_context():
        from app import routes
        db.create_all() # Cria as tabelas, se ainda não existirem

    return app
