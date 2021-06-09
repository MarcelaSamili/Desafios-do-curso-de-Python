#Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo,
# desconsiderando os espaços.
'''Um palíndromo é uma palavra, frase ou qualquer outra sequência de unidades
que tenha a propriedade de poder ser lida tanto da direita para a esquerda
como da esquerda para a direita. Num palíndromo, normalmente são desconsiderados
os sinais ortográficos, assim como o espaços entre palavras'''
frase = str(input('Digite uma frase:')).strip().upper()
palavra = frase.split()
junto = ''.join(palavra)
inverso = ''              # da pra fazer sem o for é so colocar ( inverso = junto[::-1] )
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
print('A frase ou palavra {} invertida fica {}'.format(junto, inverso))
if junto == inverso:
    print('Essa frase é um Palindromo')
else:
    print('Essa frase não é um palindromo')