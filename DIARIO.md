Desenvolvedor(Aluno): Mdrs-Arthur(Arthur Vinícius)
Data: 22/10/2026
O que foi feito: A implementação de arquivos HTML. A implementação foi feita a partir de um arquivo base e subdivisões para cada tela.
Dificuldade encontrada: Devido ter apenas criado o HTML, não encontrei nenhuma dificuldade.
Como resolvi: -
Próximo passo: Iniciar a parte de controladores e modelos do sistema.

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Desenvolvedora(Aluna): wemylly(Wemylly Joice)
Data: 22/10/2026
O que foi feito: Nesse commit eu criei os arquivos database.py e models.py, onde no database foi desenvolvido somente o básico e no models tentei criar as classes padrão e fazer alguns relacionamentos (que tinham erros).
Dificuldade encontrada: Nessa primeira parte minha dificuldade foi relacionada a como seria o database, quais funções iam ser necessárias no futuro e quais tabelas eu precisaria fazer naquele momento.
Como resolvi: Alguns erros continuaram pertinentes, mas sobre quais classes e funções seriam necessárias eu compreendi conversando com meus colegas para alinhar o que queríamos fazer no projeto 
Próximo passo: Na minha parte o próximo passo seria corrigir os erros presentes, terminar as tabelas, corrigir os relacionamentos e adicionar os que ficaram pendentes, além de implementações necessárias

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Desenvolvedora(Aluna): wemylly(Wemylly Joice)
Data: 23/10/2026
O que foi feito: Nessa atualização eu não realizei muitas alterações, de forma que alterei apenas o models.py , excluindo algumas tentativas de relacionamento anteriores que estavam erradas e tentando corrigir algumas.
Dificuldade encontrada: Tive algumas dificuldades de logística no relacionamento entre usuário e empréstimo.
Como resolvi: Reavaliando todas as tabelas que seriam necessárias e quais relacionamentos entre elas seriam lógicos e proveitosos para o projeto.
Próximo passo: Terminar a criação das tabelas e as funções.

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Desenvolvedora(Aluna): wemyllyj-droid(Mariana Sâmara)
Data: 26/10/2026
O que foi feito: implementação de blueprints e rotas em um deles
Dificuldade encontrada: relacionar as rotas com o html através das variáveis que deveriam ser exibidas no template, além disso, não conseguir testar o código.
Como resolvi: fiz pesquisas sobre o jinja e como ele se comportava nesse relacionamento de rota pra template e fui tentando até conseguir combinar as variáveis entre eles. A parte de testar não consegui realizar.
Próximo passo: Testar o código e implementar o outro blueprint, além de fazer mais algumas rotas.

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Desenvolvedora(Aluna): wemylly(Wemylly Joice)
Data: 27/10/2026
O que foi feito: O arquivo models.py foi drasticamente alterado, de forma que terminei todos os relacionamentos de forma correta, adicionei informações as tabelas e fiz funcionar, no arquivo database.py eu comecei algumas funções de crianção e de busca (mas errei em fazer todo manual, e não usando orm ), já no seed eu adicionei algumas informações.
Dificuldade encontrada: Principalmente na implantação do relacionamento n:n, pois precisava criar uma tabela associativa.
Como resolvi: Pesquisando por meio dos slides do gsa como o professor ensinou essa questão, realizei pesquisas no Google para ver modelos que usavam esse estilo e testei diversas vezes até rodar.
Próximo passo: Corrigir as funções.

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Desenvolvedor(Aluno): Mdrs-Arthur(Arthur Vinícius)
Data: 29/10/2026
O que foi feito: Reorganização de algumas partes do projeto e alterações nos arquivos para que o código se tornasse funcional.
Dificuldade encontrada: A maior dificuldade encontrada foi que ao criar o banco ele não criava as tabelas junto. Também tive algumas dificuldades com erros de escrita.
Como resolvi: Fiz várias alterações no database e no models para ver se chegava até a solução do problema, porém só consegui resolver quando importei o arquivo models para o app.
Próximo passo: Incrementar o Sqlalchemy.orm e codificar as rotas relacionadas à entidade livro.

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Desenvolvedora(Aluna): wemylly(Wemylly Joice)
Data: 30/10/2026
O que foi feito: Corrigi toda a parte das funções, criando várias outras que ainda não existiam (como toda a parte de busca de livro ), passei tudo pro padrão orm , adicionei informações a tabela livros no models.py, corrigi todo o seed.py e adicionei informações, além de corrigir erros bobos de escrita e criar e rodar o banco de fato .
Dificuldade encontrada: A transformação de estilo
Como resolvi: Buscando pelos slides do professor e exemplos na internet 
Próximo passo: Pedir para meus colegas testarem e realizarem suas funções

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Desenvolvedor(Aluno): Mdrs-Arthur(Arthur Vinícius)
Data: 30/10/2026
O que foi feito: A implementação da função de listagem de livros, a rota e o HTML para a tala de perfil, de livros e de detalhe de livro, e fiz algumas alterações no cadastro e login.
Dificuldade encontrada: Minha principal dificuldade foi a diferença entre as duas sessions, a do flask e a do banco.
Como resolvi: Resolvi através de pesquisa, consultas na documentação e ajuda da IA para relembrar a diferença entre ambas.
Próximo passo: Desenvolver mais a parte das rotas do livro.

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Desenvolvedora(Aluna): wemyllyj-droid(Mariana Sâmara)
Data: 31/10/2026
O que foi feito: implementei o emprestimo, a devolução deixei as pesquisas funcionais, exibi o autor e a qtd de exemplares no detalhar e corrgi a função criar_livro para inserir mais livros
Dificuldade encontrada: relacionar as rotas com o html através das variáveis que deveriam ser exibidas no template, além disso, tive muita dificuldade na rota de emprestimo pois não sabia muito bem como fazer já que envolvia muitas informações de tabelas diferentes. A devolução foi bem mais simples.
Como resolvi: por tentativa e erro, fui testando as formas que daria certo e consultando o arquivo onde definimos os relacionamentos. Além disso pesquisei como relacionar algumas informações na rota e da rota pro html.
Próximo passo: Certificar que tudo esteja funcional e sem quebrar.

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Desenvolvedor(Aluno): Mdrs-Arthur(Arthur Vinícius)
Data: 31/10/2026
O que foi feito: A implementação de parte do CRUD de livros, como excluir e editar. E adicionei a restrição de algumas rotas apenas para usuários Adm.
Dificuldade encontrada: A falha na função de exigir_login e após a exclusão do livro desejado do banco apresentava erro no banco de dados e quebrava sistema.
Como resolvi: Comecei a usar o retorno que vinha da função exigir_login. Analisei o banco e criei uma função para que na hora que fosse excluir um livro excluísse também os exemplares relacionados.
Próximo passo: Teste do codigo por todos os desenvolvedores.