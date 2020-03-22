from datetime import datetime
import yaml

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# path is unique to local machine
yaml_path = '../../../../Projects/perionet/perionet_sensitive.yaml'
with app.open_resource(yaml_path) as f:
    sensitive_info = yaml.safe_load(f)
app.config['SECRET_KEY'] = sensitive_info['secret_key']

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
db = SQLAlchemy(app)

# IMPORTANT!!! 'from app import routes' must be done below this comment!
# to save without auto-format, press Ctrl + K then Ctrl + Shift + S
from app import routes
