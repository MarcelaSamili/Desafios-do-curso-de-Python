from desafio115aula.sistema.menu import *

def arquivoexiste(nome):
    try:
        listadados = open(nome, "rt")
        listadados.close()
    except FileExistsError:
        return False
    else:
        return True

def criaraquivo(nome):
    try:
        listadados = open(nome, "wt+")
        listadados.close()
    except:
        print('Houve um erro na cração do arquivo')
    else:
        print('Arquivo criado com sucesso')

def leraquivo(nome):
    try:
        a = open(nome, "rt")
    except:
        print('Por algum motiv nao consegui ler o arquivo')
    else:
        cabecalho('PESSOAS CADASTRADAS'.center(30))
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        a.close()



def cadastrar(arq, nome='desconhecido', idade=0):
    try:
        a = open(arq, 'at') #at = append arquivo de texto
    except:
        print('Algo deu errado na abetura do arquivo')
    else:
        try:
            a.write(f'{nome}; {idade}\n ')
        except:
            print('Ouve um erro ao escrever o arquivo')
        else:
            print(f'Novo registro de {nome} adiciondo!')
            a.close()