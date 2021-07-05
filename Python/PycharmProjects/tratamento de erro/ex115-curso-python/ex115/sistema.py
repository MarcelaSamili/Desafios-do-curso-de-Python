from ex115.lib.interface import *
from time import sleep
from ex115.lib.arquivo import *


arq = 'cadastro.txt'

if not arquivoExiste(arq):
    CriarArquivo(arq)


while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema'])
    if resposta == 1:
      # Opção de cadastrar pessoas
        lerArquivo(arq)
    elif resposta == 2:
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome:'))
        idade = leiaint('Idade:')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabecalho('Saindo do sistema')
        break
    else:
        print('ERRO opção inválida')
    sleep(2)