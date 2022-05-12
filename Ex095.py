# 095

print('-' * 50)

jogadores, gols = [], []
totalGols = 0

while True:
    jogador = str(input('Jogador: '))
    quantPartidas = int(input('Quant. de partidas: '))

    for i in range(quantPartidas):
        quantGols = int(input(f'Quant. de gols [partida {i + 1}]: '))
        gols.append(quantGols)

        totalGols += quantGols
    
    jogadores.append({'jogador': jogador, 'gols': gols[:], 'totalGols': totalGols})

    gols.clear()
    totalGols = 0

    print('-=' * 25)
    conf = str(input('Continuar? [S/N] ')).strip().lower()[0]
    print('-=' * 25)
    if conf == 'n':
        break

print(f'{"CÓD.":<4}', f'{"Nome":<15}', f'{"Gols":<15}', f'{"Total":<6}')
print('-' * 50)
for n, i in enumerate(jogadores):
    print(f'{n:<4}', f'{i["jogador"]:<15}', f'{str(i["gols"]):<15}', f'{i["totalGols"]:<6}')
print('-' * 50)

while True:
    try:
        dados = int(input('Mostrar dados de qual jogador? [999 para sair] '))
    except ValueError:
        print('ERRO! Valor inválido! Tente novamente.')
        continue
    if dados == 999:
        break
    if dados > len(jogadores) - 1:
        print('ERRO! Valor inválido! Tente novamente.')
        continue
    if dados < 0:
        print('ERRO! Valor inválido! Tente novamente.')
        continue

    print(f'— LEVANTAMENTO DO JOGADOR {jogadores[dados]["jogador"]}: ')
    for n, i in enumerate(jogadores[dados]['gols']):
        print(f'  No jogo {n + 1} fez {i} gols.')
    print('-' * 50)