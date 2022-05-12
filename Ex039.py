# 039

from datetime import date

nascimento = int(input('Digite o ano em que você nasceu: '))
idade = date.today().year - nascimento

if idade < 18:
    print(f'Falta(m) {18 - idade} ano(s) para você ter que se alistar ao exército.')

elif idade == 18:
    print('Está na hora de você se alistar ao exército')
    
else:
    print(f'Você está {idade - 18} ano(s) atrasado no alistamento ao exército.')