from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = '38d8626329795e446589fb7e670f6797'

from perionet import routes
