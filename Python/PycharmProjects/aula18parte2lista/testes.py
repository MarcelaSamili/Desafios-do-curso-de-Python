'''teste = []
teste.append('Marcela')
teste.append(22)
galera = list()
galera.append(teste[:])
teste[0] = 'Marcos'
teste[1] = 14
galera.append(teste[:])
print(galera)'''

'''galera = [['Marcela', 20], ['Joao', 10], ['Pedro', 25], ['Ana', 14]]
print(galera)
print(galera[0][0])
print(galera[3][1])
for pessoa in galera:
    print(f'{pessoa[0]} tem {pessoa[1]} anos de idade.')'''

galera = list()
dado = list()
totmaior = totmenor = 0
for cc in range(0, 3):
    dado.append(str(input('Nome:').strip().title()))
    dado.append(int(input('Idade:')))
    galera.append(dado[:])
    dado.clear()
for p in galera:
    if p[1] >= 18:
        print(f'{p[0]} é maior de idade!')
        totmaior += 1
    else:
        print(f'{p[0]} é menor de idade!')
        totmenor += 1

print(f'tivemos {totmaior} maior/s de idade e {totmenor} menor/s de idade.')