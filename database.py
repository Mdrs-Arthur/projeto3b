from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase , Session 

class Base(DeclarativeBase):
    pass

engine = create_engine("sqlite:///biblioteca.db")

SessionLocal = Session(bind=engine)

def criar_banco ():
    Base.metadata.create_all(engine)
    
    
#precisa fazer o escopo dessas funções que vão popular o banco e fazer buscas
def criar_usuario():
    pass

def buscar_u_p_email():
    pass

def buscar_u_p_id():
    pass