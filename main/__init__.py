from flask import Flask
from main import key

app = Flask(__name__)
app.secret_key = key.SECRET_KEY

import main.views