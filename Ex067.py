# 067

num, resultado = 0, 0

while True:
    try:
        num = int(input('Quer ver a tabuada de qual valor? '))
    except ValueError:
        print('-' * 40)
        print('Valor inválido.')
        print('-' * 40)
        continue

    print('-' * 40)

    if num < 0:
        print('Encerrando a tabuada!')
        break

    for index in range(1, 11):
        resultado = num * index 
        print(f'{num} x {index:>2} = {resultado}')

    print('-' * 40)

