# 081

lst = []
count = 0

while True:
    val = int(input('Valor: '))
    lst.append(val)
    count += 1

    conf = str(input('Continuar? [S/N] ')).strip().lower()[0]
    if conf == 'n':
        break

lst.sort(reverse=True)

print(f'Você digitou {count} valores.')
print(f'Você digitou os valores: {lst}')
print(f'Você {"digitou" if 5 in lst else "não digitou"} o valor 5.')