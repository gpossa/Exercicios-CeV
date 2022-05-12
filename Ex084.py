# 084

lst, dado = [], []
pessoaP, pessoaL = [], []
maiorPeso, menorPeso, count = 0, 0, 0

while True:
    dado.append(str(input('Nome: ')))
    dado.append(float(input('Peso: ')))

    lst.append(dado[:])

    if count == 0:
        menorPeso = dado[1]

    if dado[1] > maiorPeso:
        maiorPeso = dado[1]
    elif dado[1] < menorPeso:
        menorPeso = dado[1]    

    count += 1
    dado.clear()

    conf = str(input('Continuar? [S/N] ')).strip().lower()[0]
    if conf == 'n':
        break
        
for pessoa in lst:
    if pessoa[1] == maiorPeso:
        pessoaP.append(pessoa[0])
    elif pessoa[1] == menorPeso:
        pessoaL.append(pessoa[0])

print('-=' * 15)
print(f'Ao todo você cadastrou {count} pessoas.')
print(f'O maior peso foi {maiorPeso} Kg. ({pessoaP})')
print(f'O menor peso foi {menorPeso} Kg. ({pessoaL})')