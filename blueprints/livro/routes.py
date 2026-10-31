from flask import render_template, redirect, url_for, session, flash, request
from sqlalchemy import select
from blueprints.livro import livro
from consultas import *
from database import SessionLocal
from models import  Livro


@livro.route('/livros')
def livros():
    titulo = request.args.get('titulo', '')
    genero = request.args.get('genero', '')

    with SessionLocal() as secao:
        busca = select(Livro)

        if titulo:
            busca = busca.where(Livro.titulo.ilike(f'%{titulo}%'))

        if genero:
            busca = busca.where(Livro.genero.ilike(f'%{genero}%'))

        livros = secao.scalars(busca).all()

        resultado = []

        for livro in livros:
            resultado.append({
                'id': livro.id,
                'titulo': livro.titulo,
                'genero': livro.genero
            })

    return render_template('livros.html', livros=resultado)

@livro.route('/detalhe/<int:livro_id>')
def detalhe(livro_id):
    with SessionLocal() as secao:
        livro = buscar_l_p_id(secao, livro_id)
        autores = [autor.nome for autor in livro.autores]
        exemplares = len(livro.exemplares)
    return render_template('detalhe_livro.html', livro = livro, autores = autores, exemplares = exemplares)
  
@livro.route('/emprestimo/<int:livro_id>')
def emprestimo(livro_id):
    exigir_login()
    usuario_id = session['usuario_id']

    with SessionLocal() as secao:
        resultado = emprestar_livro(secao, livro_id, usuario_id)

    if resultado:
        flash('Empréstimo realizado com sucesso!')
        return redirect(url_for('auth.perfil'))
    else:
        flash('Nenhum exemplar disponível no momento!')

    return redirect(url_for('livro.detalhe', livro_id=livro_id))

@livro.route('/devolucao/<int:livro_id>')
def devolucao(livro_id):

    exigir_login()

    usuario_id = session['usuario_id']

    with SessionLocal() as secao:
        resultado = devolver_livro(secao, livro_id, usuario_id)

    if resultado:
        flash('Livro devolvido com sucesso!')
    else:
        flash('Empréstimo não encontrado!')

    return redirect(url_for('auth.perfil'))

@livro.route('/cadastrar_livro', methods=['GET', 'POST'])
def cadastrar_livro():
    if request.method == 'POST':
        titulo = request.form['titulo']
        autores = request.form['autor']
        ano = request.form['ano']
        genero = request.form['genero']

        with SessionLocal() as secao:
            resultado = criar_livro(secao, titulo, ano, genero, autores)

        if resultado:
            flash('Livro cadastrado com sucesso!')
        else:
            flash('Autor não encontrado!')

        return redirect(url_for('livro.livros'))

    return render_template('cadastro_livro.html')

