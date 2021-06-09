# Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
#EQUILÁTERO: todos os lados iguais
#ISÓSCELES: dois lados iguais, um diferente
#ESCALENO: todos os lados diferentes
a = float(input('Me dê um dos lado:'))
b = float(input('Me dê ourto lado:'))
c = float(input('Me dê mais um lado:'))
if a+b>c>a-b and a+c>b>a-c or b+c>a>b-c:
    print('Esses lados formam um triangulo!')
    if a == b == c:
        print('Esse triangulo é EQUILÁTERO')
    if a != b != c != a:#aqui poderia ser um "elfi"
        print('Esse tringulo é ESCALENO')
    if a == b != c or a == c != b or c == b != a:#e aqui poderia ser um "else" aí nao precisaria fazer a condição
        print('Esse triangulo é ISÓCELES')
else:
    print('\033[31mESSES LADOS NÃO FORMAM TRINGULO!')
