from flask import render_template
from blueprints.livro import livro
from consultas import listar_livros, buscar_l_p_id
from database import SessionLocal

@livro.route('/livros')
def livros():
    with SessionLocal() as secao:
        livros = listar_livros(secao)
    return render_template('livros.html', livros = livros)

@livro.route('/detalhe/<int:livro_id>')
def detalhe(livro_id):
    with SessionLocal() as secao:
        livro = buscar_l_p_id(secao, livro_id)
    return render_template('detalhe_livro.html', livro = livro)