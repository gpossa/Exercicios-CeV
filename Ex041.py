# 041

from datetime import date

nascimento = int(input('Digite o ano em que você nasceu: '))
idade = date.today().year - nascimento

print(f'A idade é: {idade}')

if idade <= 9:
    print('Categoria Mirim')

elif idade >= 9 and idade <= 14:
    print('Categoria Infantil')

elif idade >= 14 and idade <= 19:
    print('Categoria Junior')

elif idade == 20:
    print('Categoria Sênior')
    
else:
    print('Categoria Master')
