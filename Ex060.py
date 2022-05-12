# 059

num = int(input('Digite um número: '))
mult = num
resultado = num

while mult != 1:
    mult -= 1
    resultado *= mult

print(f'O fatorial de {num} é {resultado}')