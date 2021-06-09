#: Faça um programa que calcule a soma entre todos os números IMPARES que são múltiplos de três
# e que se encontram no intervalo de 1 até 500.
cont = 0
soma = 0
for n in range(1, 501, 2):
    if n % 3 == 0:
        cont = cont + 1#e aqui toda quez que ele encontrar um numero que dividido por 3 da 0 ele vai somar 1
        soma = soma + n#o que vai acontecer aqui é que toda vez que ele encontar um valor que dividido por 3 da zero ele vai somar e somar cumulndo os valore
print('A soma de todos os {} valore é {}'.format(cont, soma))
