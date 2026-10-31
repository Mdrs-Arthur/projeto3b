from flask import Flask, render_template, redirect, url_for
from database import criar_banco
from blueprints.auth import auth
from blueprints.livro import livro
import models

app = Flask(__name__)
app.secret_key = 'projeto3'

criar_banco()
app.register_blueprint(auth)
app.register_blueprint(livro)

@app.route('/')
def index():
    return render_template('index.html')
