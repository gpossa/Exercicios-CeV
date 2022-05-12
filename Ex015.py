# 015

kmPercorridos = float(input('Quantos Km foram percorridos com o carro? '))
dias = int(input('Por quantos dias o carro foi alugado? '))
valor = (kmPercorridos * 0.15) + (dias * 60)

print('O valor a se pagar pelo aluguel do carro será R${:<.2f}'.format(valor))