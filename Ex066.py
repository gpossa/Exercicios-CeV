# 066

num, soma, count = 0, 0, 0

while True:
    try:
        num = int(input('Digite um número [999 para parar]: '))

    except ValueError:
        print('Valor inválido.')
        continue

    if num == 999:
        break

    soma += num
    count += 1

print(f'Você digitou {count} números. A soma deles é {soma}.')

