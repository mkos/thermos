import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SECRET_KEY'] = "X\xc9i\xef\xf3'\x8a\xc0\x9d)~\xbbf\x89\xdd,C\x90[\xfe\xa41\xe3\xfd"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'thermos.db')
db = SQLAlchemy(app)

import models
import views