# 017

import math

catOposto = float(input('Qual o valor do cateto oposto? '))
catAdjacente = float(input('Qual o valor do cateto adjacente? '))
hipotenusa = math.hypot(catOposto, catAdjacente)

print('O comprimento da hipotenusa é: {:<.2f}'.format(hipotenusa))