import moeda


num = float(input('Digte um preço: R$'))
taxa = float(input('Qual a taxa:%'))
print(f'A metade de {moeda.moeda(num)} é {moeda.metade(num, True)}')
print(f'O dobro de {moeda.moeda(num)} é {moeda.dobro(num, True)}')
print(f'Aumentando {taxa}% de {moeda.moeda(num)} temos {moeda.aumento(num,taxa, True)}')
print(f'Diminuindo {taxa}% de {moeda.moeda(num)} temos {moeda.diminuir(num, taxa, True)}')