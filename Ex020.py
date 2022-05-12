# 020

import random

arrAlunos = []

for index in range(0, 4):
    elemento = input('Digite o nome do {}º aluno: '.format(index + 1))
    arrAlunos.append(elemento)

ordem = random.sample(arrAlunos, 4)

print('A ordem de aprensetação será: {}'.format(ordem))