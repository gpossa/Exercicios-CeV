# 109

from LibsEx import moeda

num = float(input('Digite o preço: R$'))
print(f'Aumentado 10%, temos {moeda.aumentar(num, 10, True)}')
print(f'Diminuindo 13%, temos {moeda.diminuir(num, 13, True)}')
print(f'O dobro de {moeda.moeda(num)} é {moeda.dobro(num, True)}')
print(f'A metade de {moeda.moeda(num)} é {moeda.metade(num, True)}')