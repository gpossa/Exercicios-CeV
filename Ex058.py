# 058

from random import randint

print('Tente adivinhar o número escolhido entre 0 e 10.')

randNum = int(randint(0, 10))
userNum = -1
tentativas = 0

userNum = int(input('Digite seu palpite: '))

while userNum != randNum:
    userNum = int(input('Você errou. Tente novamente: '))
    tentativas += 1

print('-' * 20)
print(f'Parabéns! Você acertou o número escolhido após {tentativas} tentativas.')



