from decouple import config
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(config("APP_SETTINGS"))


bcrypt = Bcrypt(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from .accounts.models import User
from .accounts.views import accounts_bp
from .core.views import core_bp

login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = "accounts.login"
login_manager.login_message = "You must be logged in to access this page."


@login_manager.user_loader
def load_user(user_id):
    return User.query.filter(User.id == int(user_id)).first()


app.register_blueprint(accounts_bp)
app.register_blueprint(core_bp)
