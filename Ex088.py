# 089

from random import sample
from time import sleep

quant = int(input('Quantos jogos? '))

print('-=' * 15)
for i in range(0, quant):
    jogo = sample(range(0, 60), 6)
    
    jogo.sort()

    print(f'Jogo {i + 1}: {jogo}')

    sleep(1)
print('-=' * 15)
