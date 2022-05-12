# 103

def ficha(nome, gols):
    return f'O jogador {nome} fez {gols} gol(s) no campeonato.'

print('-' * 30)

jogador = str(input('Nome do Jogador: ')).strip()
if jogador == '':
    jogador = '<desconhecido>'

numGols = input('Número de Gols: ')
if not numGols.isnumeric():
    numGols = 0
    
print(ficha(jogador, numGols))