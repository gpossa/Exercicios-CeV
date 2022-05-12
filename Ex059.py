# 059

index = -1

val1 = int(input('Digite o primeiro valor: '))
val2 = int(input('Digite o segundo valor: '))
print('-' * 20)

while index != 5:
    index = int(input('O que você deseja fazer: \n[1] Somar os valores \n[2] Multiplicar os valores \n[3] Saber qual o maior dos valores \n[4] Digitar novos valores \n[5] Sair do programa \n'))
    print('-' * 20)

    if index == 1:
        print(f'A soma dos valores é: {val1 + val2}')
        print('-' * 20)

    elif index == 2:
        print(f'A multiplicação dos valores é: {val1 * val2}')
        print('-' * 20)

    elif index == 3:
        print(f'O maior valor é: {max(val1, val2)}')
        print('-' * 20)

    elif index == 4:
        val1 = int(input('Digite o primeiro valor: '))
        val2 = int(input('Digite o segundo valor: '))
        print('-' * 20)

    elif index == 5:
        print('Finalizando programa. ')

    else:
        print('Opção inválida. Digite novamente.')
        print('-' * 20)


    