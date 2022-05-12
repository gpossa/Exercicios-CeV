# 051

termo = int(input('Qual o primeiro termo da P.A.? '))
razao = int(input('Qual a razão da pra P.A.? '))

for index in range(0, 10):
    print(f'O {index + 1:>2}º termo dessa P.A é: {index * razao + termo}')