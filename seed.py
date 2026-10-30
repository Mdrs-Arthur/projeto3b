from models import Livro,Exemplar,Autor

def popular_banco(session):

     livro1 = Livro(titulo='dom quixote', ano=1000,genero='romance') 

     autor1 = Autor(nome='machado de assis')

     exemplar = Exemplar(titulo='dom quixote')

     livro1.autores = [autor1]
     exemplar.livros = livro1

     session.add_all([livro1,autor1,exemplar])
     session.commit()