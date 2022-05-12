# 079

lst = []

while True:
    val = int(input('Valor: '))
    if val in lst:
        print('Valor pulado. (Já adicionado)')
    else:
        lst.append(val)

    conf = str(input('Continuar? [S/N] ')).strip().lower()[0]
    if conf == 'n':
        break

lst.sort()

print(f'Você digitou os valores: {lst}')