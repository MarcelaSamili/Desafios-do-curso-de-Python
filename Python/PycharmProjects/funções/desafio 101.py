# Crie um programa que tenha uma função chamada voto() que vai receber
# como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal
# indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.
def voto(ano):
    from datetime import date
    idade = date.today().year - ano

    if 18 <= idade <= 69:
        return f'Com {idade} anos o voto é OBRIGATÓRIO!'
    elif idade >= 70:
        return f'Com {idade} anos o voto é OPICIONAL!'
    else:
        return f' Com {idade} anos o voto é NEGADO!'


nasc = int(input('Ano de nascimento:'))
print(voto(nasc))