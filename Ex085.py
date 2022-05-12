# 085

lst = [[], []]

for i in range(0, 7):
    val = int(input(f'Valor {i + 1}: '))
    
    if val % 2 == 0:
        lst[0].append(val)
    else:
        lst[1].append(val)

lst[0].sort()
lst[1].sort()

print('-=' * 15)
print(f'Valores pares: {lst[0]}')
print(f'Valores ímpares: {lst[1]}')