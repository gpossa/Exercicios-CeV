# 53

from unidecode import unidecode

frase = input('Digite uma frase: ')
fraseF = unidecode(frase.replace(' ', '').lower())

if fraseF == fraseF[::-1]:
    print('A frase é um palíndromo')
else:
    print('A frase não é um palíndromo')