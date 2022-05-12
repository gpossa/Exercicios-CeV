# 061

termo = int(input('Qual o primeiro termo da P.A.? '))
razao = int(input('Qual a razão da pra P.A.? '))
index = 0

while index <= 9:
    print(f'{index * razao + termo} → ', end='')
    index += 1

print('FIM', end='')