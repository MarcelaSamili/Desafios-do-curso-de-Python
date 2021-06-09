num = []
maior = menor = 0
pos = 0
cont = 0
for contador in range(0, 5):
    valor = int(input('Digite um valor: '))
    if contador == 0:
        maior = menor = valor
        num.append(valor)

    else:

        while valor > maior:
            maior = valor
            num.append(maior)

        while valor < menor:
            menor = valor
            num.insert(0, menor)

        if valor < maior and valor > menor:
            cont = valor








    print(num)

