# 019

import random

arrAlunos = []

for index in range(0, 4):
    elemento = input('Digite o nome do {}º aluno: '.format(index + 1))
    arrAlunos.append(elemento)

sorteado = random.choice(arrAlunos)

print('O aluno sorteado foi: {}'.format(sorteado))