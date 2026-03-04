import pymysql
pymysql.install_as_MySQLdb()

from flask import Flask, render_template
from config import Config
from app.extensions import db, login_manager, migrate

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app, db)

    from .auth import auth_bp
    app.register_blueprint(auth_bp)

    from .models import User, Pastel
    
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    @app.route('/')
    def index():
        pasteles = Pastel.query.all()
        return render_template('index.html', pasteles=pasteles)

    return app