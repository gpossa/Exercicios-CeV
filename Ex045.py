# 045

from random import randint

jogadaPC = randint(1, 3)

while True:
    try:
      jogadaPl = int(input('[1] Pedra \n[2] Papel \n[3] Tesoura \nEscolha uma jogada: '))
    except ValueError:
        print('Opção inválida. Tente novamente.\n')
        continue

    if jogadaPl > 3 or jogadaPl < 1:
        print('Opção inválida. Tente novamente.\n')
        continue

    else:
        break

print('-' * 27)

if jogadaPC == 1:
    print('O computador jogou: pedra.')

    if jogadaPl == 1:
        print('Você jogou: pedra.')
        print('-' * 27)
        print('Resultado: empate')
    
    if jogadaPl == 2:
        print('Você jogou: papel.')
        print('-' * 27)
        print('Resultado: você ganhou')

    if jogadaPl == 3:
        print('Você jogou: tesoura.')
        print('-' * 27)
        print('Resultado: você perdeu')

elif jogadaPC == 2:
    print('O computador jogou: papel.')

    if jogadaPl == 1:
        print('Você jogou: pedra.')
        print('-' * 27)
        print('Resultado: você perdeu')
    
    if jogadaPl == 2:
        print('Você jogou: papel.')
        print('-' * 27)
        print('Resultado: empate')

    if jogadaPl == 3:
        print('Você jogou: tesoura.')
        print('-' * 27)
        print('Resultado: você ganhou')

else:
    print('O computador jogou: tesoura.')

    if jogadaPl == 1:
        print('Você jogou: pedra.')
        print('-' * 27)
        print('Resultado: você ganhou')
    
    if jogadaPl == 2:
        print('Você jogou: papel.')
        print('-' * 27)
        print('Resultado: você perdeu')

    if jogadaPl == 3:
        print('Você jogou: tesoura.')
        print('-' * 27)
        print('Resultado: empate')

input()