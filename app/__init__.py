from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 'fasdoadfnasdof@5#$%#$sadnas'
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:01696989188@localhost/attt?charset=utf8mb4"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

db = SQLAlchemy(app=app)
login = LoginManager(app=app)
