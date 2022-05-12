# 055

pesos = []

for index in range(0, 5):
    peso = float(input(f'Digite o peso da {index + 1}º pessoa: '))
    pesos.append(peso)

pesos.sort()

print(f'O menor peso é: {pesos[0]}Kg \nO maior peso é: {pesos[4]}Kg')
