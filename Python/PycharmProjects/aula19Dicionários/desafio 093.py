# Crie um programa que gerencie o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogou.
# Depois vai ler a quantidade de gols feitos em cada partida. No final,
# tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

d = {}
lista_gols = []
soma = 0
d['nome'] = str(input('Nome do jogador:')).strip().title()
partidas = int(input(f'Quantas partidas o {d["nome"]} jogou:'))
for n in range(0, partidas):
    gols = int(input(f' Quantos gols na partida {n+1}?'))
    soma += gols
    lista_gols.append(gols)
    d['gols'] = lista_gols
    d['total'] = soma
print('-'*30)
print(d)
print('-'*30)
for k, v in d.items():
    print(f'no campo {k} tem o valor de {v}')
print('='*30)
print(f'O jogador {d["nome"]} jogou {partidas} jogos.')
for i, v in enumerate(lista_gols):
    print(f'  ->Na partida {i+1} fez {v} gols')
print('='*30)
#jeito da aula
'''d = {}
lista_gols = []
d['nome'] = str(input('Nome do jogador:')).strip().title()
partidas = int(input(f'Quantas partidas o {d["nome"]} jogou:'))
for n in range(0, partidas):
    lista_gols.append(int(input(f' Quantos gols na partida {n+1}?')))
d['gols'] = lista_gols[:] # na de cima vc teve de fazer aquilo tudo pq esquecu de por que era uma copia...
d['total'] = sum(lista_gols)'''