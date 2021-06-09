#Faça um programa que mostre a tabuada de vários números,
# um de cada vez, para cada valor digitado pelo usuário.
# O programa será interrompido quando o número solicitado for negativo.
while True:
    m = int(input('\033[34mDigite o número que vc quer a tabuada:\033[m'))
    print('\033[37m***\033[m'*5)
    if m < 0:
        break
    for n in range(0, 11):
        print(f'\033[36m{m} x {n} = {m * n}\033[m')
    print('\033[37m***\033[m'*5)
print('\033[1;39;40mPROGRAMA TABUADA ENCERRADA, VOLTE SEMPRE!\033[m')
