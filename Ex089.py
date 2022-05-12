# 089

lst, dado = [], []

while True:
    dado.append(str(input('Nome: ')))
    dado.append(float(input('Nota 1: ')))
    dado.append(float(input('Nota 2: ')))
    dado.append((dado[1] + dado[2]) / 2)

    lst.append(dado[:])

    dado.clear()

    conf = str(input('Continuar? [S/N] ')).strip().lower()[0]
    if conf == 'n':
        break

print('-=' * 15)
print(f'{"No.":<4} {"NOME":<18} MÉDIA')
print('-' * 30)

for idx, pessoa in enumerate(lst):
    print(f'{idx:<4} {pessoa[0]:<18} {pessoa[3]:<.1f}')

print('-' * 30)

while True:
        inpt = int(input('Mostrar notas de qual aluno? [999 para interromper] '))
        if inpt == 999:
            break

        print(f'Notas de {lst[inpt][0]} são {lst[inpt][1]} e {lst[inpt][2]}')
        
        print('-' * 30)