'''cont = 0
soma = 0
for contador in range(1, 501):
    if contador % 2 == 1 and contador % 3 == 0:
        cont += 1
        soma = soma + contador
print(f'A somade todos os {cont} números foi: {soma} - ', end='')
print('Fim')'''

'''print('TABUADA')
contador = 0
valor = float(input('Voce uqer a tabuada de qual número? :'))
for multiplo in range(0, 10):
    contador += 1
    multiplo *= valor
    print(f'{valor} X {contador} = {multiplo} ')'''
'''soma = 0
for contador in range(0, 6):
    valor = int(input('Digite um número:'))
    if valor % 2 == 0:
        soma += valor
print(f'A soma dos números pares são {soma}')'''

'''#frequencia de fibronacci
numero = int(input('Digite um número:'))
primeiro_termo = 0
segundo_termo = 1
print('0 - 1 - ', end='')
for contador in range(3, numero):
    soma = primeiro_termo + segundo_termo
    print(f'{soma} - ', end='')
    primeiro_termo =segundo_termo
    segundo_termo = soma
print('Fim')'''
#primo

n = int(input('Digite um número:'))
cd = 0
c = 1
while True:

    if n % c == 0:
        cd += 1
    else:
        cd += 0

    c += 1

    if c >= n:
        break

if cd < 2 or cd == 2:
    print(f'O valor {n} é primo')
else:
    if cd != 2 or cd > 2:
        print(f'O valor {n} não é primo')






