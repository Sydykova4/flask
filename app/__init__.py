from flask import Flask
from .extensions import db, migrate, login_manager

from app.config import Config

from app.routes.user import user
from app.routes.post import post


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    app.register_blueprint(user)
    app.register_blueprint(post)

    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    # LOGIN MANAGER
    login_manager.login_view = 'user.login'
    login_manager.login_message = 'вы не можете получить доступ к данной странице. Сначала авторизуйтесь. '

    with app.app_context():
        db.create_all()

    return app

