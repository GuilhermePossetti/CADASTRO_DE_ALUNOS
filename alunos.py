"""
Sistema de cadastro de alunos com persistência em SQLite.

Permite cadastrar, listar, buscar e excluir alunos através de um menu no terminal.
"""


#============ Banco de dados ==============
import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_NAME = 'BD_alunos.sqlite3'
DB_FILE = ROOT_DIR / DB_NAME
TABLE_NAME = 'alunos'

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()



# criando tabela no banco de dados
cursor.execute(
    f'CREATE TABLE IF NOT EXISTS {TABLE_NAME}'
    '('
    'id INTEGER PRIMARY KEY AUTOINCREMENT,' \
    'alunos TEXT'
    ')'
)
connection.commit() 



# função que insere um aluno no banco de dados
def cadastrar_aluno():
    aluno = input('Digite o nome do aluno: ')

    if aluno == '' or not aluno.replace(' ', '').isalpha():
        print('Nome Invalido (use apenas letras)')
        return
    
    sql = (
        f'INSERT INTO {TABLE_NAME}'
        '(alunos)'
        'VALUES'
        '(?)'
    )
    cursor.execute(sql, (aluno,))
    connection.commit()
    print(f'Aluno {aluno} cadastrado com sucesso')



# função que vai no banco de dados e lista o valor que tem lá dentro
def listar_aluno():
    cursor.execute(f'SELECT * FROM {TABLE_NAME}')
    resultado = cursor.fetchall()

    if len(resultado) == 0:
        print('Nenhum aluno na lista')
    else:
        print('\nLista de alunos: ')
        for id_aluno, nome_aluno in resultado:
            print(id_aluno, nome_aluno)
    return resultado 


# função que entra no banco de dados e busca o nome que o usuário digitou
def buscar_aluno():

    nome = input('Digite o nome do aluno que deseja buscar:')

    while True:
        if nome == '' or not nome.replace(' ', '').isalpha(): 
            nome = input('Digite o nome do aluno que deseja buscar:')        
        else:
            break

    cursor.execute('SELECT * FROM alunos WHERE alunos LIKE ?', (f'%{nome}%',))

    resultado = cursor.fetchall()

    if len(resultado) == 0:
        print('Aluno não encontrado')
    else:
        print(f'Aluno {nome} encontrado')
        for id_aluno, nome_aluno in resultado:
            print(id_aluno, nome_aluno)


# função que o usuario escolhe o id do banco de dados e exclui
def excluir_aluno():
    listar_aluno()

    try:
        escolha = int(input('Digite o ID do aluno que deseja excluir: '))

        cursor.execute('SELECT * FROM alunos WHERE id = ?', (escolha,))
    except ValueError:
        print('Digite apenas numero válidos')
        return

    verificacao = cursor.fetchall()

    if len(verificacao) == 0:
        print('Escolha inválida')
    else:
        cursor.execute(
            f'DELETE FROM {TABLE_NAME} WHERE id = ?',
            (escolha,)
        )
        print('Aluno excluido')
        connection.commit()



# interface para o usuário escolher a opção desejada
def menu():
    while True:
        print('\n === ESCOLHA UMA OPÇÃO ===')
        print()
        print('1 - Cadastrar')
        print('2 - Listar')
        print('3 - Buscar')
        print('4 - Excluir Aluno')
        print('5 - Sair')
        print()
        opcao = input('\nDigite a opção escolhida: ')
        print()
        if opcao == '1':
            cadastrar_aluno()

        elif opcao == '2':
            listar_aluno()

        elif opcao == '3':
            buscar_aluno()

        elif opcao == '4':
            excluir_aluno()

        elif opcao == '5':
            print('Acabou')
            break
        else:
            print('Opção inválida')



# Se eu estiver rodando este arquivo diretamente → execute.
if __name__ == '__main__':
    menu() 




