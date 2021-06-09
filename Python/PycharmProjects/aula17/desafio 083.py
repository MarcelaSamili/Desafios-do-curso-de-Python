#Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
# Seu aplicativo deverá analisar se a expressão passada está
# com os parênteses abertos e fechados na ordem correta.

'''lista = list()
pa = ' '
pf = ' '
while True:
    exprecao = str(input('Digite a expreção:')).strip()
    pa = exprecao.count('(')
    pf = exprecao.count(')')

    if exprecao[0] == '(':
        if pa == pf:
            print('Expreção válida')
        else:
            print('Expreção inválida')
    else:
        print('Expreção inválida')

    cond = ' '
    if cond not in 'SN':
        cond = str(input('Quer continuar?:[S/N]')).strip().upper()[0]
        if cond == 'N':
            break
print()
print('Programa encerrado')'''

#
lista = list()
exprecao = str(input('Digite a expreção:')).strip()
pa = exprecao.count('(')
pf = exprecao.count(')')
lista.append(exprecao)
for i, exprecao in enumerate(lista):
    if exprecao[i] == '(':
        if pa == pf:
            print('Expreção válida')
        else:
            print('Expreção inválida')
    else:
        print('Expreção inválida')
    print(exprecao[i]) # assim...

#solução da aula
'''exprecao = str(input('Digite uma expreção:'))
lista = []
for simb in exprecao:
    if simb == '(':
        lista.append('(')
    elif simb == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
if len(lista) == 0:
    print('Expreção Válida')
else:
    print('Expreção inválida')'''




