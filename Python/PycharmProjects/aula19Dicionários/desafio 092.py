# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário.
# Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
# Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
from datetime import date
from time import sleep
d = {}
d['nome'] = str(input('Nome:')).strip().title()
d['ano'] = int(input('Ano de nascimento:'))
anoatual = date.today().year
d['idade'] = anoatual - d['ano']
d['ctps'] = int(input('Carteira de trabalho:(0 para nao tem):'))
if d['ctps'] != 0:
    d['contratacao'] = int(input('Ano de contratação:'))
    d['salario'] = float(input('Salário:R$'))
    d['aposentadoria'] = d['idade'] + (d['contratacao'] + 20) - anoatual
    if d['idade'] >= 70:
        d['aposentadoria'] = 'Aposentado!'
    else:
        d['aposentadoria'] = d['aposentadoria']
else:
    print()
print('-'*30)
for k, v in d.items():
    print(f' -{k} tem valor -> {v}')
    sleep(0.5)