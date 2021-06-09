from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from main import key

app = Flask(__name__)
app.config.from_object('main.config')

db = SQLAlchemy(app)

import main.views