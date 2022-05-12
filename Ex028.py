# 028

from random import randint

print('Tente adivinhar o número escolhido entre 0 e 5.')
randNum = int(randint(0, 5))
userNum = int(input('Digite um número: '))

if userNum == randNum:
    print('Parabéns, você adivinhou o número! :)')
    
else:
    print(f'Você errou! Pensei no número {randNum} :(')