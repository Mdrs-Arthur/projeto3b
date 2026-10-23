from typing import List

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database import Base, criar_banco

class Usuario(Base):
    __tablename__ = "Usuarios"

    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)
    nome: Mapped[String] = mapped_column(String(80), nullable=False)
    email: Mapped[String] = mapped_column(String(80), unique=True)



class Livro(Base):
    __tablename__ = "Livros"

    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)
    titulo: Mapped[String] = mapped_column(String(100), nullable=False)

    Exemplares: Mapped[List["Exemplar"]] = relationship(back_populates="Livros")

class Exemplar(Base):
    __tablename__ = "Exemplares"

    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)
    titulo: Mapped[String] = mapped_column(String(100), nullable=False)
    quantidade: Mapped[int] = mapped_column(int)

    id_livro: Mapped[int] = mapped_column(ForeignKey("Livro.id"))
    id_exemplar: Mapped[int] = mapped_column(ForeighKey("Exemplares.id"))

    Livros: Mapped["Livro"] = relationship(back_populates="Exemplares")
    emprestimo: Mapped["Emprestimo"] = relationship(back_populates="exemplar")


class Emprestimo(Base):
    __tablename__ = "Emprestimos"

    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)

    id_exemplar: Mapped[int] = mapped_column(ForeighKey("Exemplares.id"))

    exemplar: Mapped["Exemplar"] = relationship(back_populates="emprestimo")


class Autor(Base):
    __tablename__ = "Autores"

    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)
    nome: Mapped[String] = mapped_column(String(100))

criar_banco()