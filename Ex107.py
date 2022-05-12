# 107

from LibsEx import moeda

num = float(input('Digite o preço: R$'))
print(f'Aumentado 10%, temos {moeda.aumentar(num, 10)}')
print(f'Diminuindo 13%, temos {moeda.diminuir(num, 13)}')
print(f'O dobro de {num} é {moeda.dobro(num)}')
print(f'A metade de {num} é {moeda.metade(num)}')
