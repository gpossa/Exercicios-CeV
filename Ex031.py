# 031

dist = int(input('Qual a distância da viagem? '))

if dist < 200:
    print(f'O preço da sua viagem será R${dist * 0.50:<.2f}')
    
else:
    print(f'O preço da sua viagem será R${dist * 0.45:<.2f}')
