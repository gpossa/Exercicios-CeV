# 035

num = []

for index in range(3):
    val = float(input(f'Digite a {index + 1}º medida: '))
    num.append(val)

num.sort()

if num[0] + num[1] > num[2]:
    print('É possível formar um triângulo com estas medidas!')
    
else:
    print('Não é possível formar um triângulo com estas medidas!')