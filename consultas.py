from flask import session, flash, redirect, url_for
from sqlalchemy import select
from models import Usuario
from models import Livro
from models import Autor
from models import Exemplar
from models import Emprestimo


#precisa fazer o escopo dessas funções que vão popular o banco e fazer buscas
#eu populei o banco no seed.py

def criar_usuario(session, nome, email, senha_hash):
    usuario = Usuario(
        nome = nome,
        email = email,
        senha_hash = senha_hash 
    )

    session.add(usuario)
    session.commit()
    return usuario 

def buscar_u_p_email(session,email):
    busca = select(Usuario).where(Usuario.email == email)
    usuario = session.scalars(busca).first()
    return usuario        
#Usuario é a classe , where só filtra e o scalars pega diretamente o objeto 

def buscar_u_p_id(session, usuario_id):
    busca = select(Usuario).where(Usuario.id == usuario_id)
    usuario = session.scalars(busca).first()

    return usuario

def buscar_u_p_nome(session, nome):
    busca = select(Usuario).where(Usuario.nome == nome)
    usuario = session.scalars(busca).first()

    return usuario

def criar_livro(session, titulo, ano, genero, autores):

    autor = session.scalar(select(Autor).where(Autor.nome == autores.strip()))

    if not autor:
        autor = Autor(nome=autores.strip())
        session.add(autor)
        
    livro = Livro(titulo=titulo, ano=int(ano), genero=genero, autores=[autor])

    session.add(livro)

    exemplar = Exemplar(titulo=titulo, livros=livro)

    session.add(exemplar)
    session.commit()

    return True

def buscar_l_p_id(session, livro_id):
    busca = select(Livro).where(Livro.id == livro_id)
    livro = session.scalars(busca).first()

    return livro

def buscar_l_p_titulo(session, titulo):
    busca = select(Livro).where(Livro.titulo == titulo)
    livro = session.scalars(busca).first()

    return livro

def buscar_l_p_ano(session, ano):
    busca = select(Livro).where(Livro.ano == ano)
    livro = session.scalars(busca).first()

    return livro

def buscar_l_p_genero(session, genero):
    busca = select(Livro).where(Livro.genero == genero)
    livro = session.scalars(busca).first()

    return livro

def buscar_l_p_autor(session, autor):
    busca = select(Livro).where(Livro.autores.any(Autor.nome == autor))
    livro = session.scalars(busca).all()

    return livro

def listar_livros(session):
    livros = session.scalars(select(Livro)).all()
    return livros
def emprestar_livro(secao, livro_id, usuario_id):

    exemplar = secao.scalar(select(Exemplar).where(Exemplar.id_livro == livro_id, Exemplar.emprestimo == None))

    if not exemplar:
        return False

    emprestimo = Emprestimo(id_exemplar=exemplar.id, id_usuario=usuario_id)

    secao.add(emprestimo)
    secao.commit()

    return True

def devolver_livro(secao, livro_id, usuario_id):
    emprestimo = secao.scalar(
        select(Emprestimo).join(Exemplar).where(Exemplar.id_livro == livro_id,Emprestimo.id_usuario == usuario_id))

    if not emprestimo:
        return False

    secao.delete(emprestimo)
    secao.commit()

    return True
# esse é diferente pq o autor é um relacionamento de livro , e n um paramentro viu (essa qual?)
#o .any ve se tem algum autor relacionado aquele livro 

#verificação de usuários para a restrição de rotas
def exigir_login():
    if 'usuario_id' not in session:
        flash('você precisa  ester logado!')
        return redirect(url_for('auth.login'))