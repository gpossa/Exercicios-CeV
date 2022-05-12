# 026

import unidecode

frase = input('Digite uma frase: ').strip()
fraseSemAcentos = unidecode.unidecode(frase)
numA = fraseSemAcentos.lower().count('a')
primeiraVez = fraseSemAcentos.lower().find('a') + 1
ultimaVez = fraseSemAcentos.lower().rfind('a') + 1

print(f'A frase tem: {numA} letras A, a posição em que aparece na primeira vez é: {primeiraVez} e a última: {ultimaVez}')