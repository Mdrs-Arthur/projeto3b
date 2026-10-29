from flask import Flask, render_template, redirect,url_for, flash, request
from werkzeug.security import check_password_hash, generate_password_hash
from database import SessionLocal
from blueprints.auth import auth
from consutas import criar_usuario, buscar_u_p_email

#verificação de usuários para a restrição de rotas
@auth.route('/segurança')
def exigir_login():
  with SessionLocal as session:
    if 'usuario_id' not in session:
        flash('você precisa  ester logado!')
        return redirect(url_for('auth.login'))

@auth.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
      senha = request.form['senha']
      nome = request.form['nome'],
      email = request.form['email'],
      senha_hash = generate_password_hash(senha)
      criar_usuario(nome, email, senha_hash)
      return redirect(url_for('index'))
    return render_template('cadastro.html')

@auth.route('/login', methods=['GET', 'POST'])
def login():
  
  with SessionLocal as session:
    if 'usuario_id' in session:
        flash('você já está logado!')
        return redirect(url_for('index'))
    
    if request.method == "POST":

        email = request.form['email']
        senha = request.form['senha']
        usuario = buscar_u_p_email(email)
        if usuario and check_password_hash(usuario.senha_hash, senha):
            session['usuario_id'] = usuario.id
            session['usuario_nome'] = usuario.nome
            flash('login realizado com sucesso!')
            return redirect(url_for('index'))

        flash("email ou senha errados.")

        return redirect(url_for("login"))

    return render_template("login.html")

@auth.route('/logout', methods=['GET', 'POST'])
def logout():
  if request.method == 'POST':
    with SessionLocal as session:
      session.clear()
      return redirect(url_for('login'))

  return render_template('index')
