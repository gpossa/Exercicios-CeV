# 054

import datetime

idade = 0
menor = 0
maior = 0

for index in range(0, 7):
    nascimento = int(input(f'Digite o ano de nascimento da {index + 1}º pessoa: '))
    idade = datetime.date.today().year - nascimento

    if idade < 21:
        menor += 1
    else:
        maior += 1
    
print(f'{maior} pessoas são maiores de 21 anos.')
print(f'{menor} pessoas são menores de 21 anos.')
