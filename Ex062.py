# 062

termo = int(input('Qual o primeiro termo da P.A.? '))
razao = int(input('Qual a razão da pra P.A.? '))
index, termosExtras, termosTotais = 0, -1, 10

while termosExtras != 0:
    termosTotais += termosExtras

    while index <= termosTotais:
        print(f'{index * razao + termo} → ', end='')
        index += 1
    print('...')

    termosExtras = int(input('Quantos termos a mais você quer saber? [0 para sair] '))

print(f'Foram exibidos {index} termos da P.A.')


