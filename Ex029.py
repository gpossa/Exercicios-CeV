# 029

velCarro = int(input('Qual a velocidade do carro? '))

if velCarro > 80:
    print('Você foi multado!')
    valMulta = (velCarro - 80) * 7
    print(f'A sua multa equivale a R${valMulta}')
    
else:
    print('Tudo certo!')
