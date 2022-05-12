# 042

num = []

for index in range(3):
    element = int(input(f'Digite a {index + 1}º medida: '))
    num.append(element)

num.sort()

if num[0] + num[1] > num[2]:
    print('É possível formar um triângulo com estas medidas!')

    if num.count(num[0]) == len(num): #verifica que todos os numeros no array sao iguais
        print('O triângulo será equilátero.')

    elif num.count(num[0]) == 2 or num.count(num[1]) == 2: #verifica se dois numeros no array sao iguais
        print('O triângulo será isóceles.')

    else:
        print('O triângulo será escaleno.')
        
else:
    print('Não é possível formar um triângulo com estas medidas!')