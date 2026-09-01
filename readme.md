Cadastro de Alunos👨‍🎓

Sistema de linha de comando para gerenciar o cadastro de alunos, desenvolvido em
Python com persistência de dados em banco de dados SQLite.

Projeto em andamento — este é um projeto de estudo, sendo melhorado continuamente 
enquanto avanço nos estudos de Python e banco de dados. Novas funcionalidades e 
melhorias são adicionadas regularmente.


Sobre o projeto

Este sistema permite gerenciar o cadastro de alunos através de um menu 
interativo no terminal, com todas as informações armazenadas de forma persistente
em um banco de dados SQLite.

O projeto começou como uma versão simples usando arquivos JSON para armazenamento,
e foi migrado para SQLite como parte do meu aprendizado sobre bancos de dados relacionais.


Funcionalidades:

Cadastrar novo aluno (com validação de nome)
Listar todos os alunos cadastrados
Buscar aluno pelo nome
Excluir aluno pelo ID
Persistência de dados em banco SQLite
Tecnologias utilizadas
Python 3
SQLite3 (biblioteca nativa do Python) — armazenamento dos dados
Pathlib — manipulação de caminhos de arquivo


Como executar o projeto

Clone este repositório:
bash
   git clone https://github.com/GuilhermePossetti/CADASTRO_DE_ALUNOS

Entre na pasta do projeto:
bash
   cd Cadastro_de_Alunos

Execute o arquivo principal:
bash
   python alunos.py


O banco de dados (BD_alunos.sqlite3) é criado automaticamente na primeira 
execução — não é necessário nenhuma configuração adicional.


Aprendizados

Durante o desenvolvimento deste projeto, pratiquei:

Migração de um sistema de persistência em JSON para um banco de dados relacional (SQLite)
Uso de consultas SQL (SELECT, INSERT, DELETE) com parâmetros seguros (prevenção de SQL Injection)
Organização e legibilidade de código, com comentários e nomenclatura consistente
Fluxo de versionamento com Git e GitHub
Próximos passos
Adicionar validação para nomes duplicados
Criar interface gráfica (Web, com HTML/CSS)
Melhorar tratamento de erros