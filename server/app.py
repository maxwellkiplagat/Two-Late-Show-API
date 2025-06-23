from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from server.config import SQLALCHEMY_DATABASE_URI, JWT_SECRET_KEY

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["JWT_SECRET_KEY"] = JWT_SECRET_KEY

db = SQLAlchemy(app)
migrate = Migrate(app, db)
jwt = JWTManager(app)

from server.models import *
from server.controllers.auth_controller import auth_bp
from server.controllers.guest_controller import guest_bp
from server.controllers.episode_controller import episode_bp
from server.controllers.appearance_controller import appearance_bp

app.register_blueprint(auth_bp)
app.register_blueprint(guest_bp)
app.register_blueprint(episode_bp)
app.register_blueprint(appearance_bp)

if __name__ == '__main__':
    app.run()
