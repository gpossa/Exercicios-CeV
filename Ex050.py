# 050

resultado = 0

for index in range(0, 6):
    num = int(input(f'Digite o {index + 1}º valor: '))

    if num % 2 == 0:
        resultado += num

print(resultado)