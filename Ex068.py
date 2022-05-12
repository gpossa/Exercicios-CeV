# 068

from random import randint

plNum, winCount = 0, 0
plChoice = ''

print('=-' * 20)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-' * 20)

while True:
    randNum = randint(0, 10)

    plNum = int(input('Digite um valor: '))
    plChoice = str(input('Par ou Ímpar? [P/I] ')).strip().lower()[0]

    print('-' * 20)
    if (plNum + randNum) % 2 == 0:
        print(f'Você jogou {plNum} e o computador {randNum}. Total de {plNum + randNum} deu PAR')
    else:
        print(f'Você jogou {plNum} e o computador {randNum}. Total de {plNum + randNum} deu ÍMPAR')
    print('-' * 20)

    if plChoice == 'p':
        if (plNum + randNum) % 2 == 0:
            print('VOCÊ VENCEU!')
            print('Vamos jogar novamente...')
            print('=-' * 20)
            winCount += 1
        else:
            print('VOCÊ PERDEU!')
            print('=-' * 20)
            print(f'GAME OVER! Você venceu {winCount} vezes.')
            break
    else:
        if (plNum + randNum) % 2 == 0:
            print('VOCÊ PERDEU!')
            print('=-' * 20)
            print(f'GAME OVER! Você venceu {winCount} vezes.')
            break
        else:
            print('VOCÊ VENCEU!')
            print('Vamos jogar novamente...')
            print('=-' * 20)
            winCount += 1