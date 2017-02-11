from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'jw secret key'
from app import views