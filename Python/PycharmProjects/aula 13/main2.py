 def menu():
    print('==='*15)
    print('{:^50}'.format("Detector de maior peso"))
    print(f'O maior peso foi o de {nome_pesado} com {maior} Kg')
    print('==='*15)

for cc in range(1, 5):
    menu()
    nome = str(input('Nome:')).strip().upper()
    peso = float(input(f'O peso de {nome}:Kg'))
    if peso > max(peso):
        maior = max(peso)
        nome_pesado = nome
    else:
        if peso < min(peso):
            menor = min(peso)
    menu()
menu()
print(f'Apessoa mais pesada foi {nome_pesado} com {maior} Kg.')



