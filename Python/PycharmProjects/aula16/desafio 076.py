#Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
# No final, mostre uma listagem de preços, organizando os dados em forma tabular.
'''print('{:-^42}'.format('Lista de compras'))
nomes = ('pao...............................R$ 2.50'), \
        ('presunto..........................R$ 4.20'), \
        ('queijo............................R$ 3.50'), \
        ('leite.............................R$ 4.00'), \
        ('cafe..............................R$ 4.00')
print('---'*14)
for n in nomes:
    print(n)
print('---'*14)'''
#JEITO DA AULA
print(f'{"Lista de compras":=^38}')
compra = ('pao',2.50,
         'queijo',3.50,
         'presunto', 4.20,
         'leite', 4.00,
         'café', 4.00)
#observando a posição dos objetos, veja que os nomes fican sempre com um numero par. E o valor ta semrpe numa posição de numero impar sendo assim...
for pos in range(0, len(compra)):
    if pos % 2 == 0:
        print(f'{compra[pos]:.<30}', end=' ')
    else:
        print(f'R${compra[pos]:>4.2f}')