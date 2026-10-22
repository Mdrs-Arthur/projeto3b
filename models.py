from typing import List

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database import Base, criar_banco

class Usuario(Base):
    __tablename__ = "Usuarios"

    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)
    nome: Mapped[String] = mapped_column(String(80), nullable=False)
    email: Mapped[String] = mapped_column(String(80), unique=True)

    Livros: Mapped[List["Livro"]] = relationship(back_populates="Usuarios")


class Livro(Base):
    __tablename__ = "Livros"

    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)
    titulo: Mapped[String] = mapped_column(String(100), nullable=False)
    id_usuario: Mapped[int] = mapped_column(ForeignKey("Usuario.id"))

    Usuarios: Mapped["Usuario"] = relationship(back_populates="Livro")
    Exemplares: Mapped[List["Exemplar"]] = relationship(back_populates="Livros")

class Exemplar(Base):
    __tablename__ = "Exemplares"

    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)
    titulo: Mapped[String] = mapped_column(String(100), nullable=False)
    quantidade: Mapped[int] = mapped_column(int)

    Livros: Mapped["Livro"] = relationship(back_populates="Exemplar")


class Emprestimo(Base):
    __tablename__ = "Emprestimos"

    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)
    id_usuario: Mapped[int] = mapped_column(ForeignKey("User.id"))

    Users: Mapped["User"] = relationship(back_populates="Books")

class Autor(Base):
    __tablename__ = "Autores"

    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)
    nome: Mapped[String] = mapped_column(String(100))

criar_banco()