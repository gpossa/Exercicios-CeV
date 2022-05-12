# 100

from random import randint
from time import sleep

def sortear(lst):
    print('Sorteando os 5 valores da lista: ', end='')

    for i in range(5):
        rand = randint(0, 10)
        lst.append(rand)
        sleep(0.5)

        print(rand, end=' ', flush=True)

    print('PRONTO!')

def somarPar(lst):
    pares = 0

    for i in lst:
        if i % 2 == 0:
            pares += i
    
    print(f'Somando os valores pares de {lst}, temos: {pares}')

nums = []
sortear(nums)
somarPar(nums)