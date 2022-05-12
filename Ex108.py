# 108

from LibsEx import moeda

num = float(input('Digite o preço: R$'))
print(f'Aumentado 10%, temos {moeda.moeda(moeda.aumentar(num, 10))}')
print(f'Diminuindo 13%, temos {moeda.moeda(moeda.diminuir(num, 13))}')
print(f'O dobro de {moeda.moeda(num)} é {moeda.moeda(moeda.dobro(num))}')
print(f'A metade de {moeda.moeda(num)} é {moeda.moeda(moeda.metade(num))}')
