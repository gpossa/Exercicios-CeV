# 011

altura = float(input('Qual a altura da parede em metros? '))
largura = float(input('Qual a largura da parede em metros? '))
area = altura * largura
tintaNecessaria = area / 2

print('A área da parede é {}m², sabendo que cada litro de tinta pinta 2m², é necessário {}L de tinta'.format(area, tintaNecessaria))
