#crie u programa que leia o nome de uma cidade e diga se ela começa ou não com a palavra santo.
cidade = str(input('Digite o nome de uma cidade:')).upper().split()
print('Vou analizar se o nome de sua cidade começa com Santo')
print('Analizando o nome da cidade...')
print(cidade[0] == 'SANTO')
