from flask import Blueprint

livro = Blueprint("livro", __name__, template_folder = 'templates')

from blueprints.livro import routes