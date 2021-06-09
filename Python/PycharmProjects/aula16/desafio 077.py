nome = 'fazenda', 'caro', 'notebook', 'agua', 'helicoptero', 'aviao'
for n in nome:
    print(f'\no nome {n} tem as vogais:', end=' ')
    for vogal in n:
        if vogal.lower() in 'aeiou':
            print(vogal, end=' ')

