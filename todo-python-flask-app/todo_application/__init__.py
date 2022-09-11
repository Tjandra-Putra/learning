from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SECRET_KEY'] = '5791628bb0b13ce0c676de280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)  # database instance

from todo_application import routes  # has to be imported at the bottom to prevent 'circular' import
