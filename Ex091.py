# 091

from operator import itemgetter
from random import randint
from time import sleep

jogo = {'Jogador 1': randint(0, 6), 
        'Jogador 2': randint(0, 6), 
        'Jogador 3': randint(0, 6),  
        'Jogador 4': randint(0, 6)}

rank = {}

for key, value in jogo.items():
    print(f'O {key} tirou o número {value}')
    sleep(1)

print('-=' * 15)

rank = sorted(jogo.items(), key=itemgetter(1), reverse=True)

for index, value in enumerate(rank):
    print(f'{index + 1}º lugar: {value[0]} [{value[1]} pontos]')
    sleep(1)