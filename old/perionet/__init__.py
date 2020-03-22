from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

file_path = os.path.abspath(os.getcwd())+"\database.db"

app = Flask(__name__)
app.config['SECRET_KEY'] = '38d8626329795e446589fb7e670f6797'  # this is an OFFLINE desktop app, no worries!
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+file_path
db = SQLAlchemy(app)

from perionet import routes
