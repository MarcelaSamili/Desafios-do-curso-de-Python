#Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do
# Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
#a) Os 5 primeiros times.
#b) Os últimos 4 colocados.
#c) Times em ordem alfabética.
#d) Em que posição está o time da Chapecoense.
print('{:-^50}'.format('BRASILEIRÃO 2021'))
tabela = 'America-MG', 'Athtico-PR', 'Atletico-GO', 'Atletico-MG', 'Bahia', 'Ceará-SC', 'Chapecoence', 'corinthias', 'Cuiabá', 'Flamengo', 'Fluminence', 'Fortaleza', 'Gremio', 'Internacional', 'Juventude', 'Palmeiras', 'Bragantino', 'Santos', 'Sport Recife', 'Sao Paulo'
print('---'*50)
print(f'Os 5 primeiros colocados são: {tabela[0:5]}')
print('---'*50)
print(f'Os quatro ultimos são: {tabela[-4:]}')
print('---'*50)
print(f'Os times em ordem alfabrica {sorted(tabela)}')
print('---'*50)
print('O Chapecoence esta no {}° lugar.'.format(tabela.index('Chapecoence')+1))