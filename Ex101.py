# 101

from datetime import date

def voto(nasc):
    idade = date.today().year - nasc 

    if idade < 18:
        print(f'Com {idade} anos: NÃO VOTA!')
    elif idade < 65:
        print(f'Com {idade} anos o voto é: OBRIGATÓRIO!')
    else:
        print(f'Com {idade} anos o voto é: OPCIONAL!')

nascimento = int(input('Digite o ano de nascimento: '))
voto(nascimento)