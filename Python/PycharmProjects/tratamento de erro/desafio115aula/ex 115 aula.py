from sistema.menu import *
from sistema.dados import *
from time import sleep

arq = 'arquivo.txt'
if not criaraquivo(arq):
    criaraquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema'])
    if resposta == 1:
        # opção de listar o conteud do arquivo
        leraquivo(arq)
    elif resposta == 2:
        cabecalho('NOVO CADASTRO'.center(30))
        nome = str(input('Nome:'))
        idade = leiaint('Idade:')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabecalho('Saindo do sistema! ate logo!')
        break
    else:
        print('\033[31mErro: digite uma opição valida\033[m')
    sleep(1)


