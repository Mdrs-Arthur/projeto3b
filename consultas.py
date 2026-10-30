from sqlalchemy import select
from models import Usuario
from models import Livro
from models import Autor


#precisa fazer o escopo dessas funções que vão popular o banco e fazer buscas
#eu populei o banco no seed.py

def criar_usuario(session,nome, email, senha_hash):
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

def criar_livro(session,titulo, ano, genero,autores):
    livro = Livro(
        titulo = titulo,
        ano = ano,
        genero = genero,
        autores = autores
    )

    session.add(livro)
    session.commit()
    return livro

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
# esse é diferente pq o autor é um relacionamento de livro , e n um paramentro viu
#o .any ve se tem algum autor relacionado aquele livro 