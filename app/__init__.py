import pymysql
pymysql.install_as_MySQLdb()

from flask import Flask
from config import Config
from app.extensions import db, login_manager, migrate

def create_app():
    app = Flask(__name__)
    
    # Cargamos la configuración de MySQL
    app.config.from_object(Config)

    # Inicializamos las extensiones con la app
    db.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app, db)

    @app.route('/')
    def index():
        return "¡App de Repostería funcionando!"

    return app