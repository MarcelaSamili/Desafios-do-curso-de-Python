# Crie um programa que tenha uma função fatorial() que receba dois parâmetros:
# o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional)
# indicando se será mostrado ou não na tela o processo de cálculo do fatorial

def fatorial(valor, show=False):
    cont = 1
    for c in range(valor, 0, -1):
        if show:
            print(f'{c}', end=' ')
            if c > 1:
                print(' X ', end=' ')
            else:
                print(' = ', end=' ')
        cont *= c
    return cont


print('='*30)
n = int(input('Quer o fatorial quanto?:'))
print(fatorial(n, show=False))
