# 093

info = {}
gols = []
totalGols = 0

info['jogador'] = str(input('Jogador: '))
quantPartidas = int(input('Quant. de partidas: '))

for i in range(quantPartidas):
    quantGols = int(input(f'Quant. gols [partida {i + 1}]: '))
    gols.append(quantGols)
    
    totalGols += quantGols

info['gols'] = gols
info['totalGols'] = totalGols

print('-=' * 15) 

print(info)

print('-=' * 15) 

for key, value in info.items():
    print(f'{key} → {value}')

print('-=' * 15)

print(f'O jogador {info["jogador"]} jogou {quantPartidas} partidas.')

for n, i in enumerate(info['gols']):
    print(f'  → Na partida {n + 1}, fez {i} gols.')

print(f'Foi um total de {info["totalGols"]} gols.')