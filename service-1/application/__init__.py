from flask import Flask, app
from flask_sqlalchemy import SQLAlchemy
from os import getenv

app=False(__name__)

app.config['SQLALCHEMY_DATABASE_URI']=getenv('DATABASE_URI')

db=SQLAlchemy(app)

from application import routes