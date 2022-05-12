# 092

from datetime import date

info = {}

info['nome'] = str(input('Nome: '))
nascimento = int(input('Ano nascimento: '))
info['idade'] = date.today().year - nascimento
info['ctps'] =  int(input('Carteira de Trabalho [0 não tem]: '))

if info['ctps'] != 0:
    info['contratacao'] = int(input('Ano contratação: '))
    info['salario'] = int(input('Salário: R$'))
    info['aposentadoria'] = (info['contratacao'] - nascimento) + 35

print('-=' * 15)

for key, value in info.items():
    print(f'{key} → {value}')




