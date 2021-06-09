valor = int(input('Quanto voce quer sacar: R$'))
r1 = r2 = r3 = r4 = 0
while True:
    while valor != 0:
        r1 = valor % 50
        d1 = r1 // 50
        if r1  50:
            r2 = r1 % 20
            d2 = r2 // 20
        elif r2 == 20:
            r3 = r2 % 10
            d3 = r3 // 10
        elif r3 == 10:
            r4 = r3 % 1
            d4 = r4 // 1
        elif r4 == 0:
                break
print(f'Deu {d1} notas de 50')
print(f'Deu {d2} notas de 20')
print(f'Deu {d3} notas de 10')
print(f'Deu {d4} notas de 1')
print('fim')