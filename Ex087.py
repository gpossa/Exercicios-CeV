# 086

lst = [[], [], []]
somaPar, soma3Col = 0, 0

for i in range(0, 3):
    lst[0].append(int(input(f'Valor [0, {i}]: ')))

for i in range(0, 3):
    lst[1].append(int(input(f'Valor [1, {i}]: ')))

for i in range(0, 3):
    lst[2].append(int(input(f'Valor [2, {i}]: ')))

print('-=' * 15)
for num in lst:
    print(f'[ {num[0]} ]', end='')
    print(f'[ {num[1]} ]', end='')
    print(f'[ {num[2]} ]')
    
    for num2 in num:
        if num2 % 2 == 0:
            somaPar += num2

    soma3Col += num[2]
    
print('-=' * 15)
print(f'Soma dos valores pares: {somaPar}')
print(f'Soma dos valores da 3º coluna: {soma3Col}')
print(f'Soma dos valores da 2º linha: {max(lst[1])}')