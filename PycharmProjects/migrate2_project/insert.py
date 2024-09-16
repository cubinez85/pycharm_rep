from flask import Flask
from app import db
from app.models import User, Post
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'app.db')

db = SQLAlchemy(app)

with app.app_context():

    # u = User(username='qwerty', email='qwerty@example.com')
    # db.session.add(u)
    # db.session.commit()
    res = db.session.query(User).all()
    print(res)
