from flask import render_template, redirect, url_for, flash, request, session
from werkzeug.security import check_password_hash, generate_password_hash
from database import SessionLocal
from blueprints.auth import auth
from sqlalchemy import select
from consultas import criar_usuario, buscar_u_p_email, buscar_u_p_id, exigir_login
from models import Emprestimo

@auth.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
      senha = request.form['senha']
      nome = request.form['nome']
      email = request.form['email']
      senha_hash = generate_password_hash(senha)
      
      with SessionLocal() as session:
        criar_usuario(session, nome, email, senha_hash)

      return redirect(url_for('auth.login'))
    return render_template('cadastro.html')

@auth.route('/login', methods=['GET', 'POST'])
def login():
  if 'usuario_id' in session:
    flash('você já está logado!')
    return redirect(url_for('index'))
  
  with SessionLocal() as secao:
    if request.method == "POST":
        email = request.form['email']
        senha = request.form['senha']
        usuario = buscar_u_p_email(secao, email)

        if usuario and check_password_hash(usuario.senha_hash, senha):
            session['usuario_id'] = usuario.id
            session['usuario_nome'] = usuario.nome
            return redirect(url_for('index'))

        flash("email ou senha errados.")
        return redirect(url_for("auth.login"))

    return render_template("login.html")

@auth.route('/logout')
def logout():
  session.clear()
  return redirect(url_for('auth.login'))

@auth.route('/perfil')
def perfil():
    exigir_login()

    with SessionLocal() as secao:
        usuario_id = session['usuario_id']
        usuario = buscar_u_p_id(secao, usuario_id)

        emprestimos = secao.scalars(
            select(Emprestimo).where(Emprestimo.id_usuario == usuario_id)
        ).all()

        livros = []

        for emprestimo in emprestimos:
            id = emprestimo .exemplar.livros.id
            titulo = emprestimo.exemplar.livros.titulo
            exemplar = emprestimo.exemplar.titulo

            livros.append({
                'id': id,
                'titulo': titulo,
                'exemplar': exemplar
            })

    return render_template(
        'perfil.html',
        usuario=usuario.nome,
        email=usuario.email,
        emprestimos=livros
    )