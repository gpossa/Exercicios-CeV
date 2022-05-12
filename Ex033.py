# 033

num = []

for index in range(3):
    val = int(input(f'Digite o {index + 1}º número: '))
    num.append(val)

num.sort()

print(f'O menor número é: {num[0]} \nO maior número é: {num[2]}')