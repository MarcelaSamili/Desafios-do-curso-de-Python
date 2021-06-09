# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
# Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem,
# sabendo que o vencedor tirou o maior número no dado.

from random import randint
from time import sleep
from operator import itemgetter
d = {'jogador1': randint(1, 6),
     'jogador2': randint(1, 6),
     'jogador3': randint(1, 6),
     'jogador4': randint(1, 6)}
ranking = []
for k, v in d.items():
    print(f'O {k} tirou {v} no dado')
    sleep(1)
ranking = sorted(d.items(), key=itemgetter(1), reverse=True)
print(f'{"RANkING":-^25}')
for i, v in enumerate(ranking):
    print(f'O {i+1}º lugar: {v[0]} com {v[1]}')
    sleep(1)