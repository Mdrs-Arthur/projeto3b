from typing import List

from sqlalchemy import ForeignKey, String, Table, Integer, Column
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database import Base

associativa_liv_aut = Table(
    "Autor_Livro",
    Base.metadata,
    Column('Autor_id', ForeignKey('Autores.id'),primary_key=True),
    Column('Livro_id', ForeignKey('Livros.id'),primary_key=True),
)

class Usuario(Base):
    __tablename__ = "Usuarios"

    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)
    nome: Mapped[str] = mapped_column(String(80), nullable=False)
    email: Mapped[str] = mapped_column(String(80), unique=True)
    senha_hash: Mapped[str] = mapped_column(String(80), nullable=False)

    emprestimos: Mapped[List["Emprestimo"]] = relationship(back_populates="usuarios")


class Livro(Base):
    __tablename__ = "Livros"

    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)
    titulo: Mapped[str] = mapped_column(String(100), nullable=False)
    ano: Mapped[int] = mapped_column(Integer, nullable=False)
    genero: Mapped[str] = mapped_column(String(100), nullable=False)


    exemplares: Mapped[List["Exemplar"]] = relationship(back_populates="livros")

    autores: Mapped[List['Autor']] = relationship(secondary=associativa_liv_aut,back_populates='livro')


class Exemplar(Base):
    __tablename__ = "Exemplares"

    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)
    titulo: Mapped[str] = mapped_column(String(100), nullable=False)

    id_livro: Mapped[int] = mapped_column(ForeignKey("Livros.id"))
    livros: Mapped["Livro"] = relationship(back_populates="exemplares")

    emprestimo: Mapped["Emprestimo"] = relationship(back_populates="exemplar",uselist=False)


class Emprestimo(Base):
    __tablename__ = "Emprestimos"

    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)

    id_exemplar: Mapped[int] = mapped_column(ForeignKey("Exemplares.id"),unique=True)
    exemplar: Mapped["Exemplar"] = relationship(back_populates="emprestimo")

    id_usuario: Mapped[int] = mapped_column(ForeignKey("Usuarios.id"))
    usuarios: Mapped["Usuario"] = relationship(back_populates="emprestimos")

class Autor(Base):
    __tablename__ = "Autores"

    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)
    nome: Mapped[str] = mapped_column(String(100))

    livro: Mapped[List['Livro']] = relationship(secondary=associativa_liv_aut,back_populates='autores')

