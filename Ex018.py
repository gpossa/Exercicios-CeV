# 018

import math

valAngulo = int(input('Digite o ângulo: '))
cos = math.cos(math.radians(valAngulo))
sen = math.sin(math.radians(valAngulo))
tan = math.tan(math.radians(valAngulo))

print('O coseno desse ângulo é: {:<.3f} \nO seno desse ângulo é: {:<.3f} \nA tangente desse ângulo é: {:<.3f}'.format(cos, sen, tan))