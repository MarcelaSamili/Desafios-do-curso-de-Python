# Crie um programa que tenha a função leiaInt(),
# que vai funcionar de forma semelhante ‘
# a função input() do Python, só que fazendo a
# validação para aceitar apenas um valor numérico. Ex: n = leiaInt(‘Digite um n: ‘)

def leiaint(msg):
    ok = False
    v = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            v = int(n)
            ok = True
        else:
            print('\033[31mESTA FORMA NÃO É VÁLIDA!\033[m')
        if ok:
            break
    return v


n = leiaint('Digite um valor n:')
print(f'Voce acabou de digitar o número {n}')