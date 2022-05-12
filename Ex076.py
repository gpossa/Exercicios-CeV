# 076

tup = ('Pão', 1.49, 'Frango', 16.99, 'Arroz', 5.99, 'Feijão', 8.99, 'Maionese', 7.99)

print('-' * 40)
print('LISTAGEM DE PREÇOS'.center(40))
print('-' * 40)

for index in range(0, len(tup), 2):
        print(f'{tup[index]:.<30} R${tup[index + 1]:>7}')

print('-' * 40, '\n')