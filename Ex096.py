# 096

def calcularArea(b, h):
    area = b * h
    print(f'A área de um terreno {b} * {h} é de {area}m²')

base = float(input('LARGURA (m): '))
altura = float(input('COMPRIMENTO (m): '))

calcularArea(base, altura)