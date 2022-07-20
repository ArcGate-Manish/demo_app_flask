
# from crypt import methods

from flask import Flask, session
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timedelta
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from smtplib import SMTP


app = Flask(__name__)
app.config['SECRET_KEY'] = "thisisrequired"
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://stonex:Stonex&123@localhost/login_sys'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
app.permanent_session_lifetime = timedelta(minutes=1)


db = SQLAlchemy(app)


login_manager = LoginManager(app)
login_manager.init_app(app)
login_manager.login_view = 'my_view.login'


# ===================================================================
#                       BLUEPRINTS
# ===================================================================
from project.views.app_views import app_blueprint
app.register_blueprint(app_blueprint)
