import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask.ext.moment import Moment
from flask_debugtoolbar import DebugToolbarExtension

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

# configure database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "X\xc9i\xef\xf3'\x8a\xc0\x9d)~\xbbf\x89\xdd,C\x90[\xfe\xa41\xe3\xfd"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'thermos.db')
app.config['DEBUG'] = True

db = SQLAlchemy(app)

# configure authentication
login_manager = LoginManager()
login_manager.session_protection = "strong"
login_manager.login_view = 'login'
login_manager.init_app(app)

# enable debug toolbar
toolbar = DebugToolbarExtension(app)

# for displaying timestamps
moment = Moment(app)

import models
import views
