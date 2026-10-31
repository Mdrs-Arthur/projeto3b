from models import Livro, Exemplar, Autor, Usuario
from werkzeug.security import generate_password_hash
from database import SessionLocal

def popular_banco(session):

     livro1 = Livro(titulo='dom quixote', ano=1000,genero='romance') 

     autor1 = Autor(nome='machado de assis')

     exemplar = Exemplar(titulo='dom quixote')

     livro1.autores = [autor1]
     exemplar.livros = livro1
     senha = '123456'
     admin = Usuario(nome = 'Adm', email = 'adm@admin', senha_hash = generate_password_hash(senha))

     session.add_all([livro1, autor1, exemplar, admin])
     session.commit()

popular_banco(session=SessionLocal())