import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secretkey'

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False

db =SQLAlchemy(app)
Migrate(app,db)

from myproject.tasks.views import tasks_blueprint
from myproject.users.views import users_blueprint

app.register_blueprint(users_blueprint,url_prefix='/users')
app.register_blueprint(tasks_blueprint,url_prefix='/tasks')

