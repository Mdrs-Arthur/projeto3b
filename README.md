# Biblioteca virtual


O projeto tem como tema o gerenciamento de uma biblioteca, permitindo organizar livros, autores, usuários, exemplares e empréstimos por meio de um sistema web. Foi desenvolvido por Arthur Vinicius Medeiros,
Mariana Sâmara Azevedo Santos e Wemylly Joice Dutra Saraiva
  - Arthur desenvolveu mais da parte dos templates e um pouco do CRUD
  - Mariana Desenvolveu a maior parte das rotas, incluindo o emprestimo e a devolução que envolveram implementar aslgumas funções em consultas.py
  - Wemylly implementou toda aparte do banco de dados e boa parte das consultas em consultas.py

## Descrição do sistema

O Sistema da Biblioteca Virtual é uma aplicação web desenvolvida com Python e Flask, utilizando SQLAlchemy para a comunicação com o banco de dados SQLite.

O sistema tem como objetivo facilitar a organização de uma biblioteca, permitindo o cadastro e a consulta de livros, autores e usuários, além do controle de exemplares disponíveis e dos empréstimos realizados.

Entre suas principais funcionalidades estão:

- Cadastro e login de usuários;
- Cadastro e consulta de livros;
- Cadastro e associação de autores aos livros;
- Consulta de livros por filtros;
- Controle de exemplares;
- Realização de empréstimos;
- Devolução de livros.

## Entidades do sistema

O banco de dados é composto pelas seguintes entidades:

- **Usuario:** armazena as informações dos usuários, como nome, e-mail e senha criptografada(com hash de senha).
- **Livro:** armazena informações dos livros, como título, ano de publicação e gênero.
- **Autor:** armazena os nomes dos autores cadastrados.
- **Exemplar:** representa cada unidade física de um livro disponível na biblioteca.
- **Emprestimo:** registra os empréstimos realizados, relacionando o usuário ao exemplar emprestado.

Além dessas entidades, existe uma tabela associativa chamada `Autor_Livro`, responsável por estabelecer o relacionamento entre livros e autores. Ela é necessária pois esse relacionamento se trata de um
N:N então precisamos realizá-lo através de uma tabela associativa.

## Explicação do relacionamento 1:N



## Explicação do relacionamento N:N


## Dependências necessárias para o bom funcionamento da aplicação:

Flask e SQLAlchemy

### Instruções para criar ou popular o banco de dados

O sistema utiliza o SQLite como banco de dados, e o SQLAlchemy é responsável pelo mapeamento das entidades e pela criação das tabelas. Ao rodar a aplicação o banco já é criado automaticamente e populado com um livro.


Para inserir os dados no banco:
o usuario deve ter o nome "Adm" para ter acesso as rotas de administrador e conseguir adicionar livros por exemplo.



## Principais dificuldades encontradas



## Declaração de autoria

Declaramos que desenvolvemos este projeto compreendendo o código entregue e que somos
capazes de explicar e modificar suas partes principais.
Uso de IA:

[ ] Não utilizei IA generativa.

[ sim ] Utilizei IA generativa e descrevo abaixo onde e como foi utilizada.

Descrição do uso, se houver:

A IA foi usada apenas para consulta e principalmente para entendermos nossos erros, que foram em sua maioria erros de digitação que passaram despercebidos. Vale ressaltar que não usamos IA para gerar código, apenas para 
entendermos onde erramos e como corrigir.
