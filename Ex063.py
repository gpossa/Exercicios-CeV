# 063

num = int(input('Digite o número de termos: '))
term1, term2 = 0, 1
count = 0

print('A Sequência de Fibonacci: ')
while count < num:
    print(f'{term1} → ', end='')

    term3 = term1 + term2

    term1 = term2
    term2 = term3

    count += 1
print('FIM')