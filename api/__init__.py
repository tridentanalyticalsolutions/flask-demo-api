from flask import Flask

app = Flask(__name__)

app.config.from_pyfile('config.py')
from .user import *

app.register_blueprint(mod,url_prefix='/V1')






