# 086

lst = [[], [], []]

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