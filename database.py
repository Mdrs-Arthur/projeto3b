from sqlalchemy import create_engine , text
from sqlalchemy.orm import DeclarativeBase , Sessionmaker

class Base(DeclarativeBase):
    pass

engine = create_engine("sqlite:///biblioteca.db")

SessionLocal = Sessionmaker(bind=engine)

def criar_banco ():
    Base.metadata.create_all(engine) 
    
#precisa fazer o escopo dessas funções que vão popular o banco e fazer buscas
#eu populei o banco no seed.py
def criar_usuario(session,usuario):
    session.execute(
        text("INSERT INTO usuarios (nome,email,senha_hash)VALUES (:nome,:email,:senha_hash)"),
        {"nome": nome, "email": email, "senha_hash": senha_hash}
    )
    session.commit

def buscar_u_p_email(session,email):
    linha = session.execute(
        text("SELECT * FROM usuarios WHERE email= :email"),
        {"email":email}
    ).fetchone()   
    return linha                 

def buscar_u_p_id(session,id):
    linha = session.execute(
        text("SELECT * FROM usuarios WHERE id = id"),
        {"id":usuario_id}
    ).fetchone()

    return linha

session = SessionLocal()
usuario = buscar_u_p_email(session, "wemylly@g.com")
print(usuario)
session.close()